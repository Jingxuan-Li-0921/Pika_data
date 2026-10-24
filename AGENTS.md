# Pika_data 项目上下文与代码导航

## 0. 当前目标与新增实现（2026-10-24，本节优先于下方历史快照）

### 自动只读验收入口

- `pika_bimanual/check.py` / `check_rig`：devices/live/episode/lerobot 四模式 CLI、JSON/Markdown 报告、退出码 PASS=0/WARN=1/FAIL=2、禁止覆盖已有报告；HDF5 仅以 r 模式读取，逐帧图像质量统计不将整段图像载入内存。
- `check_images.py`：共用逐帧像素摘要、近黑图、最长连续相同画面统计；0.5 秒连续相同为疑似冻结/静态场景 WARN，不能代替视觉验收。
- `check_lerobot.py`：在独立 LeRobot 环境强制离线读取，重算因果索引、核对来源/manifest/rig 契约并逐帧比较 state/action/所有 RGB 像素/task/episode-frame-global index/时间戳；不局限于首中尾抽查，保留 preview/synthetic 警告。
- 本轮修复：live 异常后保留时间戳高水位；文件拒绝源时间倒退；相机逐间隔估计掉帧，不仅看平均帧率；像素比较剔除行填充并统一颜色顺序。`camera_expected_hz` 默认 30 Hz，与当前硬件 launch 相机配置一致。
- `test_check_camera_regressions.py` 对三个相机逐个注入掉一帧/局部像素冻结/时间戳冻结/倒退/NaN/未来/缺流；`test_check_lerobot.py` 使用真实库、两个 episode 和逐帧变化数据验证多种篡改。
- `pika_bimanual/check_devices.py`：仅 stat/access、sysfs、`ip -j -details -statistics link show`；不打开字符设备、不配置 CAN、不校准；支持显式 synthetic 设备清单。
- `pika_bimanual/check_live.py`：仅订阅 Image/JointState/PoseStamped；检查两侧执行端与 Sense、相机及因果同步；无运动 publisher、服务客户端或自动驱动启动。
- `test/test_check.py`：设备别名/串号/CAN 异常，正常/缺图/错时/损坏/黑图/重复图/间隔数据，模拟时间流和真实隔离 ROS mock 订阅回归；静态限制检查模块不得引入运动接口。
- 使用方法见 README 第二部分第 5 节。报告 PASS 不等于机械标定、真实左右映射或运动验收；人工待验事项与 synthetic 标记必须保留。

### 本轮复查修复（同日，优先于旧验证记录）

- `pika_bimanual/teleop.py`：双侧 TCP/手柄时间差检查；`/pika/teleop_state` JSON 心跳包含 enabled/stamp/epoch，暂停立即通知下游。
- `pika_bimanual/runtime.py`：遥操状态联锁、心跳失效关闭输出、重设基线后拒绝旧 IK；正式录制发生暂停/失效时终止为 partial，恢复不拼接。
- 新增 `pika_bimanual/ik.py`：包装已安装的既有 IK 类，仅新入口使用 `guarded_ik`；按关节名重排反馈、检查反馈/目标年龄及求解后 FK 位姿残差，失败发布空目标使缓存失效。真实求解器仍来自 pika_remote_agx_arm，不复制或修改其子模块。
- `pika_bimanual/storage.py`：固定字段集合、形状/单位/图像/时间检查；`inspect_episode` 在回放/转换前拒绝损坏、截断、不同步或非法动作的数据。
- 新增 `pika_bimanual/export_lerobot.py`：HDF5 → 官方 LeRobot v3 image 数据集；独立 `lerobot==0.4.4` 环境，默认拒绝 preview，整帧按控制时间因果重采样，超限缺口报错，保存原始行/时间映射，finalize 后用官方读取器验证。保留 HDF5 原始档案；转换失败只留 partial，不上传 Hub。
- 新增 `requirements-lerobot.txt`：独立转换环境依赖，不能装进 ROS Python；环境在 `.analysis/lerobot-venv`（容器路径创建），参考 README 安装/使用。
- 新增 `test/test_audit.py`：错相三相机、损坏文件、字段漂移、重采样和真实 LeRobot 往返；`test/test_ik_offline.py`：真实 Pinocchio/SciPy 可达/不可达目标及乱序反馈。
- `test/test_runtime_control.py`：暂停关闭输出、正式录制中止、心跳过期/旧基线目标拒绝；`test/test_serial_offline.py` 增加静默伪串口及退出检查。
- `sensor_tools/src/serial_gripper_imu.cpp`：接收前 poll 最多等待 20 ms，避免静默串口无限占住命令互斥锁并阻止退出；仍不宣称覆盖真实 USB 拔插/固件故障恢复。
- 复查日志：`.analysis/bimanual-audit-build.log`、`.analysis/bimanual-audit-test.log`、`.analysis/lerobot-roundtrip-test.log`。测试均无设备映射；真实模型和实机验收未执行。

LeRobot 字段 `observation.state` / `action` 顺序仍是左右各 6 rad + 夹爪 m；原始 RGB uint8 HWC 转为官方读取器 CHW float32 0–1 时，在线模型适配器须作相同预处理。保存格式一致不等于模型已完成归一化或动作块适配。

用户确认：双 Sense + Station Pro 示教，保留双 Piper，末端替换成双 Pika Gripper；采集与部署使用 Gripper 左右鱼眼，后续增加 RealSense D435 全局 RGB。Sense 的相机不进入策略观测。已授权代码修改和离线验证，未授权本轮执行实机运动。

新增独立 ROS Python 包 pika_ros/src/pika_bimanual，保留旧入口，不把旧 Piper 原装夹爪启动文件直接改成新硬件。overlay 源码包数由 11 增至 12。

### 0.1 为什么不能只改相机 topic

- 旧链路把六轴和 gripper 一并交给 Piper CAN 原装夹爪，新 Pika Gripper 必须走独立 USB 串口。
- 旧 open_multi_gripper 会自动开额外 D405，并有 Sense 数据直通夹爪的 remap；新 launch 显式拆分控制、观测、示教。
- 旧固件 Command 和软件双击有双重 toggle 风险；新流程关闭固件触发并使用幂等 SetBool 遥操开关及独立录制服务。
- 旧 HDF5 转换会裁剪夹爪维度，采集和部署没有共同 observation 定义；新包直接使用统一 14 维状态/动作 + 2/3 路 RGB 的版本化格式。
- 替换末端后，旧 0.13 m TCP 不再是可信标定；默认配置留空，硬件 launch 要求明确填写。

### 0.2 新文件职责（相对 pika_ros/src/pika_bimanual）

| 文件 | 职责 |
| --- | --- |
| config/rig.yaml | 单一设备/topic/同步/限速/模型配置；D435 默认关闭，标定默认未确认 |
| launch/rig.launch.py | 默认不启硬件；hardware 显式启 Piper、Sense/Gripper、鱼眼和可选 D435；policy 模式不启 Sense/定位/IK |
| pika_bimanual/core.py | 不依赖 ROS 的字段排序、宽度验证、时间戳缓冲/同步、observation、示教 target、限位/限速门、模型 factory |
| pika_bimanual/teleop.py | 双侧幂等 clutch；共同捕获新手柄/TCP 基线；保留原定位时间戳；数据过期暂停 |
| pika_bimanual/runtime.py | ROS 适配、共用 RGB 处理、目标路由、门控、录制服务、policy 调用和状态统计 |
| pika_bimanual/storage.py | 流式 HDF5、独占编号、partial 完成提交、元数据及离线读取 |
| pika_bimanual/mock.py | 无设备的模拟相机/关节/定位输入；不创建真实控制 publisher |
| pika_bimanual/replay.py | 从保存的 observation 调用策略，验证契约并输出预测；不发布 ROS 命令 |
| test/test_core.py | 维度/顺序、过期与同步、门控、文件防覆盖、回放 |
| test/test_launch.py | 默认无硬件、模式互斥、TCP 和 D435 序列号要求 |
| test/test_ros_offline.py | 实际 ROS launch、三相机、HDF5、teleop/policy、预览无物理命令 |
| test/test_runtime_control.py | 内存 publisher 验证六轴/夹爪分流、失效关闭、幂等双侧基线 |
| test/test_serial_offline.py | 编译后的 serial_gripper_imu + 伪串口；设备绝对别名、空/NaN 命令、输出门和位置协议 |
| setup.py、setup.cfg、package.xml、resource/ | ament_python 安装与依赖 |
| .gitignore | 排除 pycache、pytest 和 egg-info 等构建产物 |

顶层 scripts/run.py 新增 bimanual（teleop/policy、mock、hardware、allow-output、config、preview-recording）和 bimanual-test（无设备、隔离 ROS domain 87）。

sensor_tools/src/serial_gripper_imu.cpp 的最小兼容修改：
- realpath 正确解析相对/绝对设备别名，替代不保证 NUL 终止并硬拼 /dev 的 readlink 用法。
- jointStateCtrlHandler 拒绝空 position 与非有限 position/effort/velocity。
- accept_commands、command_events_enabled 默认 true 保持旧入口；新 launch 明确关闭 Sense 控制和固件事件，Gripper 仅在允许输出的硬件模式接受命令。
- accept_commands=false 不等于纯被动监听：驱动启动仍有电流配置/LED 等管理写入。没有更改固件协议或重写原串口线程。

### 0.3 新链路与数据契约

示教：Sense 位姿 → 新 clutch → 既有 Pinocchio/SciPy IK → 六轴目标；Sense 宽度独立进入目标组装。
观测：Piper 编码器六轴 + Pika Gripper 实测宽度 + Gripper 两路鱼眼 + 可选 D435。
目标/反馈齐全且新鲜 → 限位/初始误差/时间与速度/跟踪检查 → Piper 六轴 topic + Pika Gripper 单宽度串口 topic。

固定顺序：left_joint1..left_joint6,left_gripper,right_joint1..right_joint6,right_gripper。六轴 rad，宽度 m；action 是绝对位置，不是 delta/TCP。
images 为 RGB uint8 HWC，尺寸由 image_size 决定；数据集与部署共用转换和同步。启用全局相机后缺帧直接拒绝，不自动改成两相机。
同步取各流最新时间中的最早值作为 anchor，并选择不晚于 anchor 的样本，限制时间差与年龄；属于软件时间对齐。
state 严格来自执行端反馈；Sense 不进入模型 observation。保留各观测源、示教源和控制发布时间戳，便于核对时延。
action 为经过守卫的已发布位置；预览时为目标值并记录 preview_only。command_published 不是硬件执行确认。
episode 使用独占 .partial，完成后链接为 .hdf5，不覆盖已有文件；中断保留 partial，后续自动跳过已使用编号。start/stop 幂等。
policy_factory 默认为 HoldPolicy，仅接口测试；接入实际模型需实现 predict(observation)->14维动作并安装所需依赖。没有训练模型、权重或训练器；LeRobot 转换入口见本轮复查说明。
新 pipeline 不使用旧 DataCapture/CaptureService，避免旧格式转换与新动作维度冲突；旧工具保留供原配置使用。

### 0.4 控制与服务

- /pika/teleop_enable（SetBool）：同时启停左右目标计算，恢复时重设基线；不是机械臂使能。
- /pika/enable_output（SetBool）：软件输出门；默认关闭，hardware_output=false 时不能开启。
- /pika/record/start、/pika/record/stop（Trigger）：独立录制，默认拒绝未开放输出的正式录制。
- /pika/target、/pika/command（JointState）：14 维期望目标与实际发布命令。
- /pika/status（String JSON）：模式、输出门、录制状态、已存帧数、丢弃计数和最近错误。
- Piper 保持 effector_type=none、auto_enable=false、control_enabled=false；真实运动仍需现场单独使能两臂与驱动门。
- 新方案不自动响应 Sense 固件 Command 或旧软件双击；不要同时启动旧 teleop/collect。

### 0.5 已验证与仍需实机确认

已完成新包及 sensor_tools 的 colcon 编译、Python 语法检查，以及单元、ROS 模拟、命令分流、伪串口离线验证。sensor_tools 仍有原有 signedness/unused 等编译警告，编译成功不代表串口硬件验收。
未启动真实机械臂、CAN、Pika 串口、鱼眼或 D435。正式上机前还需：
1. 测量新 TCP 和检查左右设备映射；当前 config 共用工具几何，左右安装不同需分侧外参。
2. 提供 D435 真实序列号、检查三 USB 视频流带宽/曝光/时间差。
3. 验证 Pika Gripper 电流、宽度零点/方向/限幅与断流保持行为。
4. 完成低幅运动、录制质量和实际模型策略验收。
5. 双臂互碰撞/环境避障未实现；软件门/限速不是完整安全控制系统。
6. 串口接收增加 poll 有界等待，伪串口覆盖静默输入/命令/退出，仍未覆盖所有真实拔插与设备恢复场景。
7. 当前鱼眼旧驱动 CameraInfo 未提供真实内参；训练 RGB 不假设已有相机标定，几何任务需另行标定。
8. 数据格式与模型输入已统一，但闭环模型效果、模型动作块时序、训练框架转换尚取决于后续选择的模型。

---

下方为上一轮原装夹爪方案的代码地图与历史快照；涉及“当前入口/配置”的表述只适用于旧 teleop/collect，不覆盖上述新 bimanual 方案。



本文供后续开发与代码修改使用；操作步骤见 README.md。最后核对：2026-10-24。
以当前源码为准；源码确认、软件运行检查和实机验证必须分别陈述，不把历史记录当作当前验收结果。

## 1. 项目目标与当前实现

双 Pika Sense + Station Pro 提供定位和手柄输入，通过 ROS 2 Humble 控制双 AgileX Piper（原装夹爪），并采集示范数据，供后续模仿学习/VLA 使用。
当前主入口是宿主机 scripts/run.py。项目已有直接遥操、隔离目标的 dry-run、独立守卫版和服务式采集；不是早期仅有单臂的状态。

当前入口对应关系（必须按实际 include 链判断，不能只读 help 或注释）：

| 宿主机入口 | ROS launch | 实际行为 |
| --- | --- | --- |
| teleop-dry-run | teleop_double_piper_dry_run.launch.py | 双臂反馈驱动 + Sense/定位 + SciPy IK；目标仅发 /dry_run；默认不启相机 |
| teleop | teleop_double_piper_runtime.launch.py | 相机/串口/定位 + teleop_double_piper.launch.py；直接控制，auto_enable=true |
| collect | collect_double_piper.launch.py | 上述直接遥操 + 双臂采集服务；不是 guarded |
| capture | data_tools/run_dual_pika_piper_capture.launch.py | 只启动采集服务，不启动传感器或机械臂 |
| 无专用 run.py 子命令 | teleop_double_piper_guarded.launch.py | dry-run + 左右 joint_command_guard；默认控制门关闭 |

run.py 中 collect 的 help 仍写 guarded，属于过时文字。直接版的 control=false 仅关闭 RViz 侧关节发布，不等于驱动的 control_enabled=false；驱动该参数默认为 true。

## 2. Host / Docker 边界

- Host：Ubuntu 20.04；负责 Docker、内核、USB、udev、SocketCAN 命名/bitrate、X11。
- Container：Ubuntu 22.04 + ROS 2 Humble，镜像 pika-data:humble；负责 ROS、定位运行库、IK、pyAgxArm、相机用户态库和采集。
- 不在容器内直接执行历史 udev/CAN 安装脚本。setup-device 由容器发现设备，宿主机安装生成的规则。
- 无参数 run.py 等价于 shell --hardware；显式 shell 默认不带硬件。
- 硬件 Compose 启用 privileged 并动态挂载整个 /dev；基础 Compose 使用 host 网络但不启用 privileged。
- 环境叠加：/opt/ros/humble → /opt/pika/vendor/install → pika_ros/install/local_setup.bash → bind-mounted pyAgxArm。
- device.env 位于容器 /root/.config/pika/device.env，entrypoint 自动加载 pika_L_code/pika_R_code。
- libsurvive 校准位于 /root/.config/libsurvive。

| 容器路径 | 来源/含义 |
| --- | --- |
| /workspace/Pika_data | 宿主机项目 bind mount，读写源码实时互通 |
| /workspace/Pika_data/pika_ros/build、install、log | 三个独立 named volumes，遮蔽宿主机同名目录 |
| /workspace/data | pika_data named volume，采集输出 |
| /root/.config | pika_config named volume，定位标定和设备变量 |

本机实际卷名为 docker_pika_build/install/log/data/config。Compose project 名改变时卷名前缀可能变化；不要硬编码为通用规则。run --rm 只删除临时容器，不删除这些卷。禁止无目的 down -v 或删除数据/校准卷。

## 3. 顶层目录与文件

| 路径 | 职责 |
| --- | --- |
| docker/Dockerfile | ROS Humble 基础镜像；安装编译/ROS/采集依赖；编译 librealsense 2.55.1；校验并解压 vendor install.zip，修复旧绝对路径、shebang 和 ELF RUNPATH；安装 ROS Pinocchio |
| docker/docker-compose.yaml | 基础开发容器、host 网络、源码挂载和持久卷 |
| docker/docker-compose.hardware.yaml | 硬件访问覆盖配置 |
| docker/entrypoint.sh | 按顺序加载 ROS/vendor/overlay/device.env，设置 SDK 和定位库搜索路径 |
| scripts/run.py | 宿主机命令入口、Compose 封装、X11 临时授权、设备安装、双臂预检和启动路由 |
| pika_ros/ | ROS 2 workspace，顶层 Git submodule |
| pyAgxArm/ | Python SDK，顶层 Git submodule |
| third_party/manifest.yaml | 初始第三方版本、归档哈希及 vendor 内容记录；其中源码 commit 已落后于当前 gitlink，不是当前版本锁定结果 |
| .gitmodules | 顶层 submodule 地址 |
| .gitignore、.dockerignore | Git 与镜像构建上下文排除规则 |
| .analysis/ | 忽略的分析及设备绑定产物；非正式源码，但 device_setup/ 是 setup-device 的实际输出，不可笼统当作可删缓存 |
| Pika 产品用户手册 beta（CN） ROS2-V2遥操测试版.md | 历史厂商参考；不能覆盖当前代码和硬件型号差异 |
| AGENTS.md | 代码地图、开发约束、当前事实和待核对项 |
| README.md | 环境配置与使用方法，不重复项目结构 |

## 4. ROS workspace 与包

pika_ros/source/ 保存 install.zip、librealsense-2.55.1.zip、curl-7.75.0.zip 等来源归档；日常启动不重复解压。
pika_ros/scripts/ 为设备配置与历史便捷脚本；其中 data_sync.py/data_to_hdf5.py 与 data_tools/scripts/ 下版本不同，不能混用参数和工作目录。

源码 overlay 有 11 个 ROS package：

| 包及路径（相对 pika_ros/src） | 职责 |
| --- | --- |
| sensor_tools/ | serial_gripper_imu.cpp 解析 Sense 串口、发布手柄/夹爪状态、触发遥操与录制；launch 管理串口、D405、鱼眼和定位 |
| data_msgs/ | Gripper、CaptureStatus 等消息与 CaptureService.srv 等服务定义 |
| data_tools/ | C++ 原始数据采集/同步/回放及 Python HDF5、MCAP、LeRobot 工具 |
| PikaAnyArm/agx_arm/pika_remote_agx_arm/ | 位姿映射、IK、双手触发协调、命令守卫及遥操 launch |
| PikaAnyArm/agx_arm/agx_arm_ros/src/agx_arm_ctrl/ | ROS 与 SDK 桥接，机械臂/夹爪控制、反馈及服务 |
| 同级 agx_arm_description/ | URDF/Xacro/mesh；agx_arm_urdf/ 是嵌套 submodule |
| 同级 agx_arm_msgs/ | 机械臂、夹爪、灵巧手消息 |
| 同级 agx_arm_moveit/ | MoveIt 配置与轨迹控制相关资源 |
| realsense-ros/realsense2_camera/ | D405 等 RealSense ROS 驱动 |
| realsense-ros/realsense2_camera_msgs/ | 相机消息 |
| realsense-ros/realsense2_description/ | 相机描述 |

pika_locator 与 libsurvive 来自 vendor underlay；当前仓库不能完整审计定位器内部二进制实现。

### 遥操关键文件

以下均相对 pika_ros/src/PikaAnyArm/agx_arm/pika_remote_agx_arm/：

- launch/teleop_double_piper_runtime.launch.py：绑定本机双 Sense 输入，组合直接遥操；相机默认开启。
- launch/teleop_double_piper.launch.py：双臂驱动、两个 delta 节点、两个 IK、右手协调器和软件双击检测；auto_enable=true、fast_mode=true。
- launch/teleop_double_piper_dry_run.launch.py：反馈模式驱动、无 GUI 定位器及隔离目标；默认关闭相机。
- launch/teleop_double_piper_guarded.launch.py：在 dry-run 上增加左右命令守卫；默认速度参数 10、目标发布 30 Hz。
- launch/collect_double_piper.launch.py：直接版 + 采集服务。
- launch/teleop_single_*、teleop_double_nero*、teleop_double_piper_x*：其他机型/历史入口，不是当前双 Piper 默认入口。
- scripts/pub_delta_pose.py：缓存手柄与 TCP 位姿；Trigger 切换 teleop_active；以基线乘手柄相对变换发布目标，默认 30 Hz。暂停只停止目标发布，不等于机械臂去使能。
- scripts/arm_ik_pose_node.py：Pinocchio 模型、IK 求解、FK 输出；auto 在 CasADi bindings 可用时使用 CasADi，否则回退 SciPy；直接版还把手柄宽度附加到关节命令。
- scripts/dual_teleop_coordinator.py：/teleop_trigger_r 并行调用左右 internal Trigger。
- scripts/sense_double_click_trigger.py：从右手 joint_state 检测开合双击，仅请求遥操 Trigger，不调用 CaptureService。
- scripts/joint_command_guard.py：初始误差、关节步长、跟踪误差、输入/反馈超时与启用门；只有 guarded launch 接入。
- config/arm_ik_pose_node.piper.yaml：Piper URDF、六轴输出、TCP z=0.13 m、优化权重与 solver_backend=auto；自碰撞检查当前 false。
- scripts/transformations.py、test_piper_sim.py：变换辅助与仿真调试；不能据文件名把后者当作无硬件风险的完整测试套件。

### 驱动、设备与 SDK

- agx_arm_ctrl/agx_arm_ctrl_single_node.py：AgxArmRosNode；按 joint name 分离六轴与 gripper；fast_mode 使用 move_js，否则 move_j。
- agx_arm_ctrl/effector/agx_gripper.py：原装夹爪封装（具体适配以当前文件为准）。
- agx_arm_ctrl/launch/start_double_piper_diagnostic.launch.py：auto_enable=false、control_enabled=false。SDK 仍可能发送查询帧，不能称为电气意义的纯被动 CAN 监听。
- sensor_tools/launch/open_multi_sensor.launch.py：左右串口、相机、locator 参数与服务 remap。
- pika_ros/scripts/setup_device.py：交互识别左右设备、生成规则/manifest/启动脚本、保存定位码；入口应使用顶层 run.py setup-device。
- pyAgxArm/pyAgxArm/api/、protocols/、extensions/、utiles/：SDK API、协议、扩展与工具；demos/、scripts/、tests/ 中可能包含真实运动/CAN 配置，不能批量直接运行。

## 5. 当前双臂调用链与接口

```text
Station Pro / Sense tracker → libsurvive → pika_locator
  /pika_pose_l、/pika_pose_r
    → pub_delta_pose + /left_arm|right_arm/feedback/tcp_pose
    → /left_delta_pose、/right_delta_pose
    → arm_ik_pose_node + feedback/joint_states + gripper_l|r/joint_state
    → /left_arm|right_arm/control/joint_states
    → AgxArmRosNode → pyAgxArm → SocketCAN → Piper / 原装夹爪
```

- 手柄：/gripper_l/data、/gripper_r/data；/gripper_l/joint_state、/gripper_r/joint_state。
- 驱动反馈：左右 /feedback/joint_states、/feedback/tcp_pose、/feedback/arm_status、/feedback/gripper_status，均在 left_arm/right_arm 命名空间下。
- 直接版 FK：/left_arm/ik_fk_pose、/right_arm/ik_fk_pose。
- dry-run 目标：/dry_run/left_arm/joint_target、/dry_run/right_arm/joint_target；FK 同目录 /fk_pose。
- SDK 关节 rad、位置/夹爪宽度 m；直接版 Sense 宽度绝对值限幅至 0.09 m，附加 name=gripper。夹爪链路已经实现，不能再描述为“缺失”。
- 右手软件双击：先张开到 >=0.07 m，再合到 <=0.02 m；两次合拢间必须重新张开，窗口 1.2 s，冷却 1 s。
- /teleop_trigger_r 是切换语义，不是幂等 enable。协调器调用左右 /teleop_trigger_l_internal、/teleop_trigger_r_internal。
- 串口固件 Command 变化也会触发遥操，并请求 CaptureService(start=true,end=true,episode_index=-1)。直接版右手 remap 到正式采集服务；左手映射到 capture_service_l。
- 软件双击本身不启动录制。固件 Command 和软件检测若都响应同一动作，存在重复切换风险，需实机核对，不能声称已去重。
- guarded/dry-run 使用左右独立 Trigger，且采集 remap 与直接版不同；dry-run IK 没有接入直接版 gripper topic，不能假定两套入口夹爪功能等价。

## 6. 数据采集和转换

| 文件（相对 pika_ros/src/data_tools） | 职责 |
| --- | --- |
| launch/run_dual_pika_piper_capture.launch.py | useService=true、allowEpisodeDelete=false、hz=-1、timeout=5、cropTime=1.0 |
| config/dual_pika_piper_data_params.yaml | 当前双臂数据通道、逻辑名称与 topic |
| src/dataCapture.cpp | DataCapture + DataCaptureService；按消息时间戳落盘，服务启动/结束 episode |
| include/dataUtility.h | 公共目录/参数/通道结构 |
| src/dataSync.cpp、scripts/data_sync.py | 时间同步；Python 版本读取 ../config，需在对应 scripts 目录运行 |
| src/dataPublish.cpp、scripts/data_publish.py | 回放 |
| scripts/data_to_hdf5.py | 同步数据转换 HDF5；参数是 --targetDir，支持 --armJointKeep；默认 useIndex=true 时输出到原 episode 目录，忽略 targetDir，并删除旧 data.hdf5 |
| scripts/hdf5_to_lerobot.py、lerobot_compute_stats.py、merge_lerobot.py | LeRobot 转换、统计、合并；默认映射需针对双臂 schema 另行核对 |
| scripts/record_mcap.py、hdf5_to_mcap.py、mcap_to_aloha_data.py | MCAP 相关工具 |
| scripts/*-b.py | 备用/历史版本，不是 README 推荐入口 |

当前配置记录：
- 4 路彩色：左右 D405 + 左右鱼眼；2 路对齐 depth。
- 关节：actionLeft/actionRight（控制命令）、feedbackLeft/feedbackRight（实测反馈）。
- TCP：targetLeft/targetRight（IK FK）与 feedbackLeft/feedbackRight。
- 定位：pika_l/pika_r；手柄编码器：pikaSensor_l/pikaSensor_r；instruction 文本。
- 原始目录为 datasetDir/episodeN，下面按 camera/color、camera/depth、arm/jointState、arm/endPose、localization/pose、gripper/encoder 等分类。
- RGB JPG、depth PNG、状态 JSON；保留各 topic 原生频率，离线同步默认容差 0.03 s。
- 重复 episode 目录在构造时拒绝；删除服务默认禁用。旧文档中的“重复 index 自动删除旧 episode”已不符合当前实现。
- episode_index=-1 表示使用服务内部计数，成功启动后递增；进程重启不扫描磁盘寻找下一个编号。
- instructions 由 launch 参数进入服务并保存；当前服务开始分支使用成员 instructions，不使用请求里的 instructions/task_* 字段。
- start=true/end=true 是切换；true/false 是开始（已有录制会先结束并重新开始）；false/true 是停止；false/false 是删除请求，默认拒绝。
- cropTime 虽传入并保存，当前文件未发现实际裁剪使用，不能承诺自动裁掉首尾一秒。
- HDF5 工具会处理/截取机械臂关节维度，不能默认等同于完整六轴+夹爪的训练 action。导出和 LeRobot 映射需单独检查。

## 7. 当前机器与验证范围

2026-10-24 SSH 检查：
- 根项目及递归 submodule 修改前均干净。
- pika-data:humble 镜像存在；无运行中的项目容器。旧 robot 容器使用 robot_image:v2，与本项目 Compose 环境不同。
- run.py doctor 通过：ROS Humble、vendor、overlay、pyAgxArm、python-can、Pinocchio、SciPy。
- device.env 保存左 LHR-B721731E、右 LHR-7485B857，libsurvive/config.json 存在。
- 当前 can_left/can_right、ttyUSB50/51、video50/51 不存在；不能据此确认硬件当前可运行。
- /workspace/data 检查时为空；本轮未做实际遥操、录制或转换验收。
- 直接版固定 D405 左 _260522276587、右 _260522272396；setup-device 不会自动重写 runtime launch 中硬编码的相机序列号。
- Station Pro 频道设置方法仍 UNKNOWN；不要套用旧硬件手册猜测。

版本快照（后续以 git submodule status --recursive 为准）：

| 仓库 | 分支/commit |
| --- | --- |
| 顶层 | main / 677079a（本轮文档修改前） |
| pika_ros | ros2 / 3fc64340f5431557cb44e110329640eb69632cb7 |
| PikaAnyArm | pika-dual-teleop / 852063e142fb5692284df1190d417b27ad4ce017 |
| agx_arm_ros | pika-dual-teleop / 457212a13d16528cdacee3e9ec3ce4acd274aad0 |
| agx_arm_urdf | main / f6642ce0d7872c686f29c99e9e10cd23d1d49313 |
| data_msgs | 0405bbaad280e0d076850fce73cdfac473c202ca |
| data_tools | pika-dual-capture / b2b952a57a0dea91da1369df964a0cbef7c1ab80 |
| pyAgxArm | master / 2255d88e1fabdf20fcd1eccbc4312b4ce1cfd2d4 |

## 8. 后续修改约束与待核对项

- 开始先读本文件、查看所有相关仓库 git status，再读对应源码。修改后检查 diff；不要覆盖用户已有修改。
- 不自动 git reset/clean/restore/stash，不删除 .git、不重初始化嵌套仓库，不自动 commit/push。
- 源码修改属于对应 submodule 仓库，父仓库随后更新 gitlink；不要把 submodule 内容作为顶层普通文件提交。
- 未明确授权不启动真实遥操、不使能机械臂、不发送运动或原始 CAN 命令、不重置急停/固件、不修改宿主机 udev/CAN。该历史阶段只授权文档更新；本轮以第 0 节的新授权为准。
- 直接版绕过 joint_command_guard，不能把守卫的超时/步长保护写成所有入口都具备。
- 协调器一侧失败后无完整回滚；软件双击与固件 Command 可能重复触发；暂停不是去使能。后续需求涉及切换语义时优先审计。
- pub_delta_pose 缓存位姿缺少输入新鲜度校验；当前自碰撞检查关闭，工作空间防护不能视为已实现。
- 数据配置对应直接版 topic；改为 guarded 时必须同步核对 FK/action 与夹爪通道。
- 后续按用户具体需求修改，不能因为本文件列出问题就自行改代码。
- 未来模型部署应明确 observation/action、坐标系、单位、频率与预处理；policy core 与 ROS1/ROS2 adapter 分离是设计方向，目前不是已存在的目录。

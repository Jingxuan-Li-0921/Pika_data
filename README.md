# 双 Sense / Station Pro / 双 Piper + Pika Gripper 数据采集与推理接口

当前目标：双 Sense 示教、Station Pro 定位，双 Piper 安装 Pika Gripper；观测使用左右 **Pika Gripper 上的鱼眼相机**，后续增加一台 RealSense D435 全局相机。Sense 相机不作为策略观测。代码结构及历史入口说明见 [AGENTS.md](AGENTS.md)。

## 第一部分：环境配置

### 1. 宿主机与 Docker

已有工程：`/home/ljx/project/Pika_data`。宿主机 Ubuntu 20.04 负责 Docker、USB/udev、SocketCAN；容器 Ubuntu 22.04 + ROS 2 Humble 负责运行和编译。宿主机需有 Docker Compose、Python 3、Git、iproute2、udev；无需在宿主机安装 ROS Humble。

```bash
cd /home/ljx/project/Pika_data
docker version
docker compose version
git status --short
git submodule status --recursive
```

新克隆使用 `git clone --recursive https://github.com/Jingxuan-Li-0921/Pika_data.git`。已有副本不要 reset 或覆盖本地修改。

已有镜像可直接编译新包，不需要重建整个镜像：

```bash
python3 scripts/run.py overlay -- build --symlink-install --packages-select sensor_tools pika_bimanual
python3 scripts/run.py doctor
python3 scripts/run.py bimanual-test
```

全新环境先 `python3 scripts/run.py build`，再 `python3 scripts/run.py overlay`。Dockerfile 使用 `pika_ros/source/install.zip` 与 `librealsense-2.55.1.zip`；启动时无需重复解压。IK 使用现有 Pinocchio + SciPy，无需另装 CasADi。

源码挂载在 `/workspace/Pika_data`；build/install/log、`/workspace/data` 和 `/root/.config` 使用持久卷。退出临时容器不删除数据。不要执行 `docker compose down -v`。

### 2. 配置两路或三路相机

配置文件：`pika_ros/src/pika_bimanual/config/rig.yaml`。建议复制到项目 `.analysis/rig.local.yaml` 后按实机修改，启动时使用对应容器绝对路径：

```bash
mkdir -p .analysis
cp -n pika_ros/src/pika_bimanual/config/rig.yaml .analysis/rig.local.yaml
```

关键设置：

| 参数 | 用途 |
| --- | --- |
| `global_camera_enabled: false` | 仅左右 Gripper 鱼眼；D435 未接入时使用 |
| `global_camera_enabled: true` | 三相机；缺少全局图像时拒绝产生完整观测，不填黑图 |
| `global_camera_serial` | D435 实际序列号，必须用字符串；真实三相机启动禁止留空 |
| `image_size: [240, 320]` | 模型图像尺寸 H/W；统一 RGB、uint8、HWC，采集/部署使用同一路径 |
| `devices.left/right` | CAN、Sense 串口、Gripper 串口、Gripper 鱼眼设备号 |
| `tcp_xyz_rpy` | Piper 驱动的真实新 TCP 外参；6 个数，平移 m、旋转 rad |
| `tool_translation_xyz`、`tool_pre_rot_rpy` | IK 的新 TCP 外参；必须与驱动对应 |
| `hardware_calibrated` | 完成安装偏置、方向和关节限制核对后才设 true |
| `task` | 本次示范任务文字，写入 episode 元数据 |

TCP 默认留空，不能照搬原装夹爪的 0.13 m。当前配置为左右共用同一工具几何，若左右安装方式不同，需要先扩展成分别标定后再上机。默认关节限位沿用现有 Piper 守卫范围，上机前与当前型号核对。

D435 只启动 RGB，不默认开启 depth；Gripper 内置 D405 也不启动。D435 输出 topic 为 `/pika/cameras/global/color/image_raw`。左右鱼眼为 `/pika/cameras/left_wrist/image_raw` 与 `/pika/cameras/right_wrist/image_raw`。

两相机与三相机数据集是不同观测契约，不能未经适配混用同一模型；回放工具会检查相机集合、尺寸和字段定义。

### 3. 后续连接硬件时的准备（本轮未执行）

先绑定双 Sense，再绑定双 Pika Gripper：

```bash
python3 scripts/run.py setup-device
# 选择 1：双 Sense，按提示识别左右
python3 scripts/run.py setup-device
# 选择 2：双 Gripper，按提示识别左右
```

应得到：Sense `/dev/ttyUSB50/51`，Gripper `/dev/ttyUSB60/61`，Gripper 鱼眼 `/dev/video60/61`。绑定后保持相同 USB 接口。setup-device 会安装宿主机 udev 规则，不能在容器里手动执行旧拓扑脚本。

```bash
ls -l /dev/ttyUSB50 /dev/ttyUSB51 /dev/ttyUSB60 /dev/ttyUSB61
ls -l /dev/video60 /dev/video61
python3 scripts/run.py exec -- cat /root/.config/pika/device.env
```

Sense 定位码仍使用 `pika_L_code` / `pika_R_code`。需要重新标定时：

```bash
python3 scripts/run.py exec --hardware -- survive-cli --force-calibrate
```

标定保存于持久卷 `/root/.config/libsurvive`，强制标定会更新现有结果，不必每次执行。Station Pro 频道设置仍需按当前设备说明确认。

宿主机正确命名并配置 `can_left`、`can_right`，1 Mbps；左右物理对应关系必须现场确认。不要在容器内改 Host CAN。检查：

```bash
ip -details link show can_left
ip -details link show can_right
```

本轮未连接真实设备；已用伪串口测试驱动，但未验证实际串口、鱼眼、D435 带宽、TCP 或运动。串口启动仍设置电流/LED 等管理信息，不是纯被动监听。新入口不会替你安装 udev、设置 CAN、标定 TCP 或自动使能 Piper。

## 第二部分：使用方法

### 1. 不连接硬件的完整验证

```bash
cd /home/ljx/project/Pika_data
python3 scripts/run.py bimanual-test
```

测试在不映射设备的容器里运行，使用 `ROS_DOMAIN_ID=87`、`ROS_LOCALHOST_ONLY=1`。覆盖字段顺序、夹爪宽度、同步/过期、限速/控制门、录制防覆盖、三相机 RGB、实际 ROS launch 和策略回放。测试中的动作发布使用内存替身，ROS 预览测试检查物理命令 topic 没有输出。

也可手动观察模拟采集。两个终端都先设置以下环境（避免接入其他 ROS 图）：

```bash
export ROS_DOMAIN_ID=87
export ROS_LOCALHOST_ONLY=1
```

终端 A：

```bash
python3 scripts/run.py bimanual --mock --preview-recording \
  --config /workspace/Pika_data/.analysis/rig.local.yaml \
  --dataset-dir /workspace/data/pika_bimanual_preview
```

设置 `global_camera_enabled: true` 可模拟三相机，mock 模式不要求真实 D435 序列号或 TCP。终端 B：

```bash
python3 scripts/run.py ros2 -- topic echo /pika/status
# Ctrl+C 结束持续查看，再执行下列命令
python3 scripts/run.py ros2 -- service call /pika/record/start std_srvs/srv/Trigger '{}'
python3 scripts/run.py ros2 -- service call /pika/record/stop std_srvs/srv/Trigger '{}'
```

start/stop 是幂等操作：重复 start 不会重启 episode。新编号自动避开已有 `.hdf5` 和 `.partial`。完成录制才把临时文件变为 `episode_000000.hdf5`；直接杀进程会保留未完成 `.partial`。不要把未完成文件或预览数据直接用于正式训练。

### 2. 数据内容与训练接口

每帧包含：

- `observation/state`：14 维，左六轴 + 左实际夹爪宽度 + 右六轴 + 右实际夹爪宽度；关节 rad，宽度 m。
- `observation/images/left_wrist`、`right_wrist`，启用时加 `global`：RGB uint8 HWC。
- `target`：示教或策略期望的 14 维绝对位置。
- `action`：控制门开放时为限速后的已发布命令；预览时为期望目标，并显式标记 `preview_only=true`。
- `command_published`：ROS 是否发布过命令，**不代表机械臂已执行成功**；实际行为看反馈。
- `timestamp`、`control_timestamp`、各输入的 `source_timestamps` / `target_timestamps`：保留观测与命令时间，可审计延迟。
- metadata：schema、完整字段顺序、单位、相机集合、任务文字及配置快照。

Sense 仅作为示教来源，不混入策略 observation；夹爪 state 来自 Pika Gripper 实测宽度。相机未齐、消息过期或时间偏差超限时不生成完整帧，`/pika/status` 报告原因及丢弃计数。同步是按 ROS header 时间戳的因果软件对齐，不等同于硬件同步。

采集保留 HDF5 原始档案，新增 **LeRobot v3 转换出口**。HDF5 能保留各路原始时间戳、target、实际 action 和异常诊断信息，后续无需重新采集即可导出其他格式；不调用会裁剪夹爪维度的旧转换脚本。训练使用 `complete=true`、`preview_only=false` 的完整 episode。读取和转换前检查维度、单位、相机集合、数据长度、时间顺序和同步范围。

LeRobot 转换使用独立 Python 环境，避免 PyTorch/NumPy 依赖影响 ROS。以下命令在项目根目录执行；首次安装需要联网，转换不上传数据：

```bash
python3 scripts/run.py exec -- bash -c 'python3 -m venv /workspace/Pika_data/.analysis/lerobot-venv'
python3 scripts/run.py exec -- env -u PYTHONPATH /workspace/Pika_data/.analysis/lerobot-venv/bin/pip install \
  torch==2.7.1 torchvision==0.22.1 --index-url https://download.pytorch.org/whl/cpu
python3 scripts/run.py exec -- env -u PYTHONPATH /workspace/Pika_data/.analysis/lerobot-venv/bin/pip install \
  -r /workspace/Pika_data/pika_ros/src/pika_bimanual/requirements-lerobot.txt
```

本机已建立该环境，后续直接运行转换。输出目录必须不存在：

```bash
python3 scripts/run.py exec -- env HF_HUB_OFFLINE=1 \
  PYTHONPATH=/workspace/Pika_data/pika_ros/src/pika_bimanual \
  /workspace/Pika_data/.analysis/lerobot-venv/bin/python -m pika_bimanual.export_lerobot \
  --episodes /workspace/data/pika_bimanual/episode_000000.hdf5 \
  --output /workspace/data/pika_lerobot --repo-id local/pika_bimanual \
  --fps 30 --max-gap 0.1
```

可在 `--episodes` 后列出多个同契约文件。默认拒绝预览数据；仅验证模拟数据时增加 `--allow-preview`。输出使用官方 `lerobot==0.4.4` 的 v3 写入器，包含 `observation.state`、`action` 和 `observation.images.{left_wrist,right_wrist,global}`，14 维顺序与单位不变。图像采用无损 image/Parquet 表示，不强制编码有损视频；官方读取器返回的图像通常是 CHW、float32、0–1，模型适配器须与在线 RGB uint8 HWC 输入做相同转换。

转换按命令时间建立固定 fps 网格，对**整帧**做因果保持，不分别插值图像与动作。超过 `--max-gap` 的空洞直接拒绝；不会把长暂停压缩成连续动作。`pika_conversion.json` 保存原始文件、配置、行号、观测/控制时间和输出时间映射。HDF5 保留为原始档案，不删除；LeRobot 输出先写 `.partial` 目录，经官方库重读确认后完成。训练前根据采样质量检查重用帧比例，并确认训练 fps 与部署频率一致。

官方格式说明：[LeRobotDataset v3](https://huggingface.co/docs/lerobot/lerobot-dataset-v3)。本项目没有添加特定模型训练器。

### 3. 策略离线回放与部署接口

默认 `HoldPolicy` 只返回当前状态，用于验证接口，不是训练好的模型。真实策略需实现：

```python
class MyPolicy:
    def __init__(self, checkpoint, **kwargs):
        # 加载自己的模型和预处理参数
        ...

    def predict(self, observation):
        # state: (14,); images: {left_wrist, right_wrist, [global]}
        # timestamp/source_timestamps/task 也可用
        # 返回 (14,) 有限数值：左六轴+夹爪、右六轴+夹爪，绝对位置
        return action
```

在配置设置 `policy_factory: your_module:MyPolicy` 和 `policy_kwargs`（例如 checkpoint 路径），并让模块在容器中可导入。归一化、模型尺寸、时序窗口、动作块展开需要由所选模型适配器处理；不能把 delta/TCP 动作直接作为此接口的关节绝对位置。

完全离线回放（无需 ROS 图、Sense 或硬件）：

```bash
python3 scripts/run.py ros2 -- run pika_bimanual replay_policy \
  --config /workspace/Pika_data/.analysis/rig.local.yaml \
  --episode /workspace/data/pika_bimanual_preview/episode_000000.hdf5 \
  --output /workspace/data/pika_bimanual_preview/predictions_000000.hdf5
```

输出只包含预测，不发送任何命令，也不覆盖已有输出。在线模拟策略：

```bash
python3 scripts/run.py bimanual --mode policy --mock --preview-recording \
  --config /workspace/Pika_data/.analysis/rig.local.yaml
```

真实部署的 policy 模式只启动 Piper 反馈、Pika Gripper 与相机，不需要 Sense、Station Pro、定位器或 IK（本接口输出的是六轴关节动作）。采集与部署使用同一观测生成函数和图像处理，模型仍需匹配相机配置与训练数据。

### 4. 实机测试操作单：双 Sense + Station Pro + 双 Piper + 双 Pika Gripper + D435

**本节是待现场执行的操作单，编写时未启动实机。** 按 4.1–4.8 顺序逐项验收，不把全部命令一次性粘贴运行。首次测试空载、清空两臂运动范围，由现场人员守住物理急停。当前无双臂互碰撞规划；软件关闭输出不等于硬件急停，夹爪可能保持最后位置。

#### 4.1 统一终端、配置和测试目录

在同一宿主机准备终端 A（运行节点）、B（服务操作）、C（观测）。**每个终端**先执行：

```bash
cd /home/ljx/project/Pika_data
export ROS_DOMAIN_ID=88
export ROS_LOCALHOST_ONLY=1
export RIG_CONFIG=/workspace/Pika_data/.analysis/rig.local.yaml
export RUN_ID=rig_acceptance_001
export CAPTURE_DIR=/workspace/data/$RUN_ID
export LEROBOT_DIR=/workspace/data/${RUN_ID}_lerobot
r2() { python3 scripts/run.py ros2 -- "$@"; }
```

88 是本操作单的现场测试域，与离线回归的 87 分开；必须先确认没有其他程序使用它。全部节点和检查命令使用相同设置。不同时启动旧 teleop/collect、mock 或 policy。再次测试时三个终端一起修改 RUN_ID；不能覆盖已有 LeRobot 输出目录。容器 `/workspace/data` 是持久卷，不是宿主机同名路径。

只在首次准备时复制配置，随后人工填写：

```bash
mkdir -p .analysis
cp -n pika_ros/src/pika_bimanual/config/rig.yaml .analysis/rig.local.yaml
nano .analysis/rig.local.yaml
```

必填：`global_camera_enabled: true`、D435 的真实字符串序列号、明确的任务 `task`、左右设备映射、实测 `tcp_xyz_rpy` / `tool_translation_xyz` / `tool_pre_rot_rpy`。确认几何和关节限制后才设置 `hardware_calibrated: true`。左右安装不同不能直接使用共用 TCP。首次运动可将 `max_joint_speed_rad_s` 降至 0.1、`max_gripper_speed_m_s` 降至 0.01；这是测试建议，不是已验证的硬件安全值。不要为通过检查而放宽时间/初始误差限制。

**验收：** 三个终端设置一致，配置不是占位值，运行目录与任务文字明确，旧流程已停止。保持 `rate_hz: 30.0`、`image_size: [240, 320]`，便于按下面的转换和检查命令验收。

#### 4.2 设备、CAN、Station Pro 检查（启动节点前）

宿主机执行：

```bash
lsusb
lsusb -t
ls -l /dev/ttyUSB50 /dev/ttyUSB51 /dev/ttyUSB60 /dev/ttyUSB61
ls -l /dev/video60 /dev/video61
readlink -f /dev/ttyUSB50 /dev/ttyUSB51 /dev/ttyUSB60 /dev/ttyUSB61
readlink -f /dev/video60 /dev/video61
ip -details -statistics link show can_left
ip -details -statistics link show can_right
python3 scripts/run.py exec -- cat /root/.config/pika/device.env
# 会访问 USB，仅在现场执行；此时不得同时运行其他 RealSense 程序
python3 scripts/run.py exec --hardware -- rs-enumerate-devices -s
```

| 设备 | 验收标准 |
| --- | --- |
| 双 Sense | 左 `/dev/ttyUSB50`、右 `/dev/ttyUSB51` 指向不同设备；`pika_L_code` / `pika_R_code` 非空、不同，并与左右实物对应 |
| Station Pro | 供电、固定安装、无遮挡；与双 Sense 定位配置对应；不凭 USB 列表就判定定位合格，必须继续验收 4.3 位姿流 |
| 双 Piper | `can_left/right` 对应已标识的左右机械臂；接口 UP，bitrate 1000000；无 BUS-OFF，运行前后错误计数不持续增长 |
| 双 Pika Gripper | 左 `/dev/ttyUSB60`、右 `/dev/ttyUSB61`；鱼眼 `/dev/video60/61` 物理归属一致；末端紧固、线缆有活动余量 |
| D435 | 枚举结果的型号和序列号与配置一致，USB 连接正常；不误选 Gripper 内的 D405；三路视频避免共用明显带宽不足的链路 |

别名未配置时按第一部分的 `setup-device` 流程处理。只在确实需要重新标定、且采集节点已停止时执行：

```bash
python3 scripts/run.py exec --hardware -- survive-cli --force-calibrate
```

完成定位标定并退出工具后再启动新管线，不并行占用定位设备。此命令会更新持久卷中的标定，不是每次测试的必需步骤。

#### 4.3 关闭输出，检查双臂反馈、Sense 与三路相机

终端 A：

```bash
python3 scripts/run.py bimanual --mode teleop --hardware \
  --config "$RIG_CONFIG" --dataset-dir "$CAPTURE_DIR"
```

这里不加 `--allow-output`。Piper 默认不自动使能且驱动控制门关闭，但串口节点启动仍会写电流/LED 等管理信息。

终端 B/C 分别运行下列检查；持续命令观察约 30 秒后 Ctrl+C 再执行下一条。`r2` 辅助命令不需要 `--hardware`，它们经 ROS 图读取已启动节点：

```bash
r2 service list -t
r2 topic echo /pika/status --once
r2 topic echo /left_arm/feedback/joint_states --once --qos-reliability best_effort
r2 topic echo /right_arm/feedback/joint_states --once --qos-reliability best_effort
r2 topic echo /pika/sense/left/joint_state --once --qos-reliability best_effort
r2 topic echo /pika/sense/right/joint_state --once --qos-reliability best_effort
r2 topic echo /pika/gripper/left/joint_state --once --qos-reliability best_effort
r2 topic echo /pika/gripper/right/joint_state --once --qos-reliability best_effort
r2 topic echo /pika_pose_l --once
r2 topic echo /pika_pose_r --once
r2 topic hz /pika_pose_l
r2 topic hz /pika_pose_r
r2 topic hz /pika/cameras/left_wrist/image_raw
r2 topic hz /pika/cameras/right_wrist/image_raw
r2 topic hz /pika/cameras/global/color/image_raw
```

图像 QoS 和原始分辨率可另外检查：

```bash
r2 topic info /pika/cameras/global/color/image_raw -v
r2 topic echo /pika/cameras/left_wrist/image_raw --once --no-arr --qos-reliability best_effort
r2 topic echo /pika/cameras/right_wrist/image_raw --once --no-arr --qos-reliability best_effort
r2 topic echo /pika/cameras/global/color/image_raw --once --no-arr --qos-reliability best_effort
```

**验收：** 左右六轴名称 joint1..joint6、数值有限且在配置范围内；夹爪反馈为单个米制宽度，范围 0–0.098 m；单独动左/右 Sense 时对应位姿和宽度变化，另一侧保持静止。手柄静止时位姿不跳变，时间戳持续前进；不得以重新打戳掩盖定位丢失。三路原始 RGB 图像配置为 640×480、目标 30 Hz，建议每路稳定观测频率至少 27 Hz、无长时停帧；CLI 频率受订阅端负载影响，最终以保存文件统计为准。真实左右视角、曝光、清晰度在 4.7 导出图像后人工确认。

此时 `/pika/status` 应为 `output_enabled=false`、`recording=false`；未启遥操时提示 paused/等待 IK 是正常的，不能据此判定相机失败。

#### 4.4 只计算遥操目标，验证映射与暂停

保持输出关闭，在终端 B 执行：

```bash
r2 service call /pika/teleop_enable std_srvs/srv/SetBool '{data: true}'
r2 topic echo /pika/teleop_state --once
r2 topic echo /pika/target --once
r2 topic echo /pika/status --once
# 检查暂停与重新建立基线
r2 service call /pika/teleop_enable std_srvs/srv/SetBool '{data: false}'
r2 topic echo /pika/status --once
r2 service call /pika/teleop_enable std_srvs/srv/SetBool '{data: true}'
```

**验收：** 服务 `success=true`；启用后在新数据到达时产生 14 维 target，左六轴+左宽度+右六轴+右宽度，状态 error 清空；小幅单侧手柄动作只改变对应目标。再次 true 不重设已有基线；false 暂停，下一次 true 重设双方基线，并丢弃旧 IK。整个阶段机械臂、夹爪不应跟随目标运动。若 IK 报残差过大，应检查 TCP/坐标轴/工作空间，不直接扩大容差（默认 0.02 m、0.15 rad）。

通过后调用 teleop false，在终端 A Ctrl+C 停止整套节点；确认退出后再进入下一阶段。重启后原先的遥操状态和软件门不会保留。

#### 4.5 空载小幅运动：逐个开放控制门

终端 A 重启：

```bash
python3 scripts/run.py bimanual --mode teleop --hardware --allow-output \
  --config "$RIG_CONFIG" --dataset-dir "$CAPTURE_DIR"
```

终端 B **逐条执行并检查响应**；以下 true 调用会逐步允许真实运动，必须已完成前面验收。两个 Sense 保持静止，宽度先接近各自 Gripper 的实测值：

```bash
r2 service call /pika/enable_output std_srvs/srv/SetBool '{data: false}'
r2 service call /left_arm/enable_agx_arm std_srvs/srv/SetBool '{data: true}'
r2 service call /right_arm/enable_agx_arm std_srvs/srv/SetBool '{data: true}'
# 两臂使能并稳定后再建立当前 TCP/手柄基线
r2 service call /pika/teleop_enable std_srvs/srv/SetBool '{data: true}'
r2 topic echo /pika/status --once
r2 topic echo /pika/target --once
r2 service call /left_arm/control_enable std_srvs/srv/SetBool '{data: true}'
r2 service call /right_arm/control_enable std_srvs/srv/SetBool '{data: true}'
# 最后开放上层输出门
r2 service call /pika/enable_output std_srvs/srv/SetBool '{data: true}'
r2 topic echo /pika/command --once
r2 topic echo /pika/status --once
```

任一服务失败就停在当前步骤，关闭已开放的门并排查。上层 success 不代表 Piper 已执行：必须同时看到两臂反馈与 Gripper 实测宽度跟踪，驱动没有忽略命令/教导模式错误。初始目标必须接近反馈：关节差不超过 0.035 rad，宽度差不超过 0.01 m；不通过时重新对齐和建立基线，不强制发送跳变位置。

依次测试左手小幅平移/转动、右手小幅平移/转动，再测试两夹爪小幅开合，最后测试两侧同时小幅动作。先做厘米级手柄位移与几毫米宽度变化，确认方向后再逐步扩大。另一侧保持静止；不直接向 `/pika/gripper/*/command` 发测试命令绕过统一守卫。

**验收：** 左右无交叉控制、动作方向正确、无突跳/持续振荡；Piper 收到六轴命令，Gripper 独立串口收到单宽度命令。无输出中断，反馈跟踪不触发关节 0.12 rad / 宽度 0.02 m 守卫（这是拒绝阈值，不是精度承诺）。空载下夹爪无异常卡滞、电流/温升；实际允许电流及额定范围以设备配置和厂家资料核对，本文不提供未经验证的电流值。

先不录制，执行一次 teleop false：

```bash
r2 service call /pika/teleop_enable std_srvs/srv/SetBool '{data: false}'
r2 topic echo /pika/status --once
```

应看到 `output_enabled=false`，后续命令停止。状态 topic 约 1 Hz，观察应在下一次状态发布体现；这不是物理急停时延保证。重新 teleop true 只恢复目标计算，必须再次调用 enable_output true 才恢复输出。心跳/输入过期的硬件故障注入留到稳定验证后单独安排，不在运动中拔线测试。

#### 4.6 三相机正式采集

恢复遥操并开放输出，确认无错误后再录制，不添加 `--preview-recording`：

```bash
r2 service call /pika/teleop_enable std_srvs/srv/SetBool '{data: true}'
r2 service call /pika/enable_output std_srvs/srv/SetBool '{data: true}'
r2 topic echo /pika/status --once
r2 service call /pika/record/start std_srvs/srv/Trigger '{}'
r2 topic echo /pika/status
# 观察 10–20 秒；完成动作后 Ctrl+C 停止上面的状态查看，再结束录制
r2 service call /pika/record/stop std_srvs/srv/Trigger '{}'
```

第一段安排：开头静止约 2 秒、依次单侧运动和开合、双侧小幅运动、结尾静止约 2 秒。三路相机覆盖同一场景，可在静止阶段让一个可见标记先后经过三个视野，便于人工核对画面与时间。记录 start/stop 返回的实际路径，编号不一定是 000000。

**验收：** start/stop 均成功，开始后 `recording=true`、frames 增长，结束返回 `.hdf5`；正常段无 error，无持续 dropped 增长。frames/dropped 是进程累计值，比较本段前后差值，不能将启动等待时期的 dropped 计入该段。文件必须包含三路图像；如果发生暂停/输入失效而得到 `.partial`，该段不作为正式训练数据，恢复后重新 start，不改后缀伪装完成。

#### 4.7 正常停机与原始文件验收

先完成 record stop，再按顺序关闭软件门、遥操和两臂驱动门：

```bash
r2 service call /pika/enable_output std_srvs/srv/SetBool '{data: false}'
r2 service call /pika/teleop_enable std_srvs/srv/SetBool '{data: false}'
r2 service call /left_arm/control_enable std_srvs/srv/SetBool '{data: false}'
r2 service call /right_arm/control_enable std_srvs/srv/SetBool '{data: false}'
```

机械臂已到可安全停放位置，按现场要求承托/确认卸力不会下落后，再关闭使能：

```bash
r2 service call /left_arm/enable_agx_arm std_srvs/srv/SetBool '{data: false}'
r2 service call /right_arm/enable_agx_arm std_srvs/srv/SetBool '{data: false}'
```

终端 A Ctrl+C 退出，随后才做离线文件检查。异常时先保证现场停止，不能为了保存完整 episode 延迟急停。

在宿主机设置 **stop 实际返回的容器路径**（下面编号只是示例），执行完整性、频率、时延和图像检查：

```bash
export EPISODE="$CAPTURE_DIR/episode_000000.hdf5"
python3 scripts/run.py exec -- env EPISODE="$EPISODE" \
  PYTHONPATH=/workspace/Pika_data/pika_ros/src/pika_bimanual python3 -c '
import os
from pathlib import Path
import h5py, numpy as np, cv2
from pika_bimanual.storage import inspect_episode
p = os.environ["EPISODE"]
meta = inspect_episode(p, allow_preview=False)
assert set(meta["cameras"]) == {"left_wrist", "right_wrist", "global"}
out = Path("/workspace/Pika_data/.analysis") / (Path(p).parent.name + "_" + Path(p).stem + "_frames")
out.mkdir(parents=True, exist_ok=True)
with h5py.File(p, "r") as f:
    t = f["timestamp"][:]
    c = f["control_timestamp"][:]
    assert len(t) >= 2
    sources = np.array([x[:] for x in f["source_timestamps"].values()])
    print("frames", len(t), "duration_s", t[-1]-t[0])
    print("effective_hz", (len(t)-1)/(t[-1]-t[0]))
    print("max_control_gap_s", np.diff(c).max())
    print("max_source_skew_s", np.ptp(sources, axis=0).max())
    print("max_age_at_command_s", (c-sources.min(axis=0)).max())
    for key in meta["cameras"]:
        images = f["observation/images/"+key]
        print(key, images.shape, images.dtype)
        for i in sorted({0, len(t)//2, len(t)-1}):
            assert cv2.imwrite(str(out/(key+"_%06d.png" % i)), cv2.cvtColor(images[i], cv2.COLOR_RGB2BGR))
print("PASS; inspect images in", out)
'
```

**硬性验收：** 脚本 PASS；complete 为 true、preview 为 false，全部 action 有发布标记，所有字段长度一致；状态/动作均为 14 维，RGB 图像为 `(N,240,320,3)` uint8；时间递增，各观测源时间差不超过配置 0.06 s、命令时最老源年龄不超过 0.25 s。保存的 action 是命令，不是“动作已经执行”的确认。

**首轮建议指标：** 有效采样频率至少 27 Hz，最大控制采样间隔不超过 0.1 s；人工打开宿主机 `.analysis/<运行名>_<episode>_frames/` 中的 PNG，确认左右视角未互换、全局画面确为 D435、颜色正常、无黑屏/严重模糊、目标和夹爪可见。PNG 抽样不能证明整段无冻结，结合本段实际运动、连续图像流和时间统计判断。若软件时间差满足但视觉动作明显错位，记录现象并排查曝光/USB/设备时钟；不要宣称已经实现硬件同步。

#### 4.8 转换为 LeRobot，并用官方读取器验收

使用 4.7 已通过检查的 EPISODE。首次转换环境安装见第二部分第 2 节；以下均无硬件访问：

```bash
python3 scripts/run.py exec -- env HF_HUB_OFFLINE=1 \
  PYTHONPATH=/workspace/Pika_data/pika_ros/src/pika_bimanual \
  /workspace/Pika_data/.analysis/lerobot-venv/bin/python -m pika_bimanual.export_lerobot \
  --episodes "$EPISODE" --output "$LEROBOT_DIR" \
  --repo-id local/pika_bimanual --fps 30 --max-gap 0.1
```

正式数据不加 `--allow-preview`。目录已存在时选择新的 RUN_ID/输出目录，不删除原数据来重试。出现 gap 错误先检查采集质量，不为通过转换直接放宽到长暂停。

```bash
python3 scripts/run.py exec -- env HF_HUB_OFFLINE=1 \
  LEROBOT_DIR="$LEROBOT_DIR" \
  PYTHONPATH=/workspace/Pika_data/pika_ros/src/pika_bimanual \
  /workspace/Pika_data/.analysis/lerobot-venv/bin/python -c '
import os, json
from pathlib import Path
import h5py, numpy as np
from lerobot.datasets.lerobot_dataset import LeRobotDataset
root = Path(os.environ["LEROBOT_DIR"])
manifest = json.loads((root/"pika_conversion.json").read_text())
ds = LeRobotDataset(repo_id="local/pika_bimanual", root=root)
assert ds.meta.info["codebase_version"] == "v3.0"
assert len(ds) == sum(len(e["source_rows"]) for e in manifest["episodes"])
offset = 0
for e in manifest["episodes"]:
    assert not e["preview_only"]
    indices = e["source_rows"]
    print("frames", len(indices), "reused_row_fraction", 1-len(set(indices))/len(indices))
    with h5py.File(e["source"], "r") as f:
        for j in sorted({0, len(indices)//2, len(indices)-1}):
            i, row = indices[j], ds[offset+j]
            np.testing.assert_allclose(row["observation.state"].numpy(), f["observation/state"][i], atol=1e-6)
            np.testing.assert_allclose(row["action"].numpy(), f["action"][i], atol=1e-6)
            for camera in ("left_wrist", "right_wrist", "global"):
                expected = f["observation/images/"+camera][i].transpose(2,0,1)/255.0
                np.testing.assert_allclose(row["observation.images."+camera].numpy(), expected, atol=1e-6)
    offset += len(indices)
print("PASS", ds.meta.info["codebase_version"], "frames", len(ds))
'
```

**验收：** 转换目录完成，不是 `.partial`；官方读取器 PASS，帧数与 manifest 一致，抽查首/中/尾的 14 维状态、动作、三图与原始行一致；米/rad 单位及顺序没有改变。官方图像为 CHW、0–1，已按原始 RGB HWC 转换后核对。建议重用原始行比例不超过 10%；超出时回查频率和丢帧，不能因转换成功就判断训练质量合格。原始 HDF5、配置快照、转换 manifest 一起保留。

本次验收记录至少填写：日期/操作者、左右设备与 D435 序列号、TCP 配置、启停服务结果、每段文件路径、帧数/有效频率/最大间隔/源时间差/年龄、视觉检查、LeRobot 帧数和重用比例。以上实机结果尚未执行或填写，离线通过不能代替现场验收。

### 5. 自动只读检查与报告

`check_rig` 提供 devices / live / episode / lerobot 四个模式，不启动驱动、不创建使能服务客户端、不发布运动命令。只写入指定的新报告目录；不会覆盖、修复或改写被检查的数据。每次输出 `report.json` 和 `report.md`，结果为 PASS / WARN / FAIL；退出码分别为 0 / 1 / 2。PASS 仅表示所列自动项目通过，不是实机运动验收。报告中的 `synthetic` 明确标记模拟检查，人工待验项目单独列出。

先编译安装入口：

```bash
cd /home/ljx/project/Pika_data
python3 scripts/run.py overlay -- build --symlink-install --packages-select pika_bimanual
python3 scripts/run.py bimanual-test
```

**离线回归（当前先执行这一项）**包含模拟设备清单、正常/损坏 HDF5、三路相机缺失/错相/过期/未来/重复时间戳、黑图/冻结图/长间隔，以及真实 ROS mock → 只读订阅检查。无需接设备，也不需要 `--hardware`。测试数据是预览或明确标记的 synthetic 数据，不是正式示范。

需要手工观察模拟检查时，先创建专用配置，将 `global_camera_enabled` 设 true（不改实机标定）：

```bash
cp -n pika_ros/src/pika_bimanual/config/rig.yaml .analysis/rig.mock.yaml
nano .analysis/rig.mock.yaml
```

两个终端均执行 `export ROS_DOMAIN_ID=87 ROS_LOCALHOST_ONLY=1`。终端 A 只启动 mock：

```bash
python3 scripts/run.py ros2 -- run pika_bimanual mock --ros-args \
  -p config:=/workspace/Pika_data/.analysis/rig.mock.yaml
```

终端 B 只订阅并生成报告：

```bash
python3 scripts/run.py ros2 -- run pika_bimanual check_rig live \
  --config /workspace/Pika_data/.analysis/rig.mock.yaml --duration 30 --synthetic \
  --report-dir /workspace/Pika_data/.analysis/check_mock_001
```

`live` 的前 2 秒留给 ROS 发现和缓冲积累，之后每个采样点做与采集一致的因果对齐；检查结束时再次检查每个流的新鲜度，避免前半段正常、后半段断流仍被判通过。检查相机、双臂反馈、Gripper/Sense 宽度和双 Sense 位姿，不依赖启用遥操或 IK。持续时间可设置 3–600 秒。

**后续实机设备检查（本轮不执行）**：设备必须已经接好，此命令仅让检查进程看到设备节点，不启动硬件驱动：

```bash
python3 scripts/run.py ros2 --hardware -- run pika_bimanual check_rig devices \
  --config /workspace/Pika_data/.analysis/rig.local.yaml \
  --report-dir /workspace/Pika_data/.analysis/check_devices_001
```

读取设备节点类型、访问权限、实际路径/设备号，检查六个别名指向不同设备；读取 CAN 状态/1 Mbps/错误统计、双定位码、USB sysfs 中 D435 型号与序列号。不打开串口/视频流、不配置 CAN、不执行标定。权限结果只代表运行检查的用户/容器；CAN 错误趋势、USB 实际带宽和左右物理归属仍需后续观察。可用 `--device-fixture /path/inventory.json` 替代真实系统读取进行离线测试，报告自动标为 synthetic。

**后续实机在线数据流检查（本轮不执行）**：按 4.3 人工启动反馈节点且保持输出关闭；检查终端使用同一 ROS 域 88，不添加 `--synthetic`：

```bash
python3 scripts/run.py ros2 -- run pika_bimanual check_rig live \
  --config /workspace/Pika_data/.analysis/rig.local.yaml --duration 30 \
  --report-dir /workspace/Pika_data/.analysis/check_live_001
```

若没有现成数据流，检查会报告缺流失败，不会替用户启动设备。异常消息数、源时间戳频率、最大间隔、末次数据年龄、因果对齐成功/失败次数和最大源偏差会写入报告。缺流、过期/未来/倒退时间戳、非法反馈或超同步范围为 FAIL；建议频率/间隔不达标为 WARN。在线不保存相机画面，不自动判断曝光、模糊或画面左右归属。

**采集文件检查（完全离线）**：stop 完成录制后指定真实文件路径：

```bash
python3 scripts/run.py ros2 -- run pika_bimanual check_rig episode \
  --config /workspace/Pika_data/.analysis/rig.local.yaml \
  --episode /workspace/data/rig_acceptance_001/episode_000000.hdf5 \
  --report-dir /workspace/Pika_data/.analysis/check_episode_001
```

检查格式完整性、14 维字段、限位、图像集合/尺寸、已发布动作、各路时间戳、源时间差、有效频率、最大间隔，并逐帧统计近黑图和相邻重复图像。静态场景也可能产生重复图像，所以此项为 WARN，不当作确定的相机冻结故障；人工仍按 4.7 抽查画面。默认拒绝 preview 数据；仅离线模拟验证可加 `--allow-preview`，此时报告保留训练来源 WARN。相机集合按配置检查，三相机验收必须使用 `global_camera_enabled: true` 的配置。

**相机异常检测说明：** 在线和文件检查都逐路统计时间间隔。除平均频率和最大间隔外，按相机预期 30 Hz 估计缺失帧数，单次漏帧也会产生 WARN；这是时间戳推算，无法区分设备掉帧、传输丢包或订阅端未及时处理。只有真实相机帧率改变时才调整配置 `camera_expected_hz`，不要把该值降低以掩盖掉帧。文件中的合法因果复用另行统计，不当作时间戳倒退。

在线检查会去掉行填充并统一 RGB/BGR 后比较像素摘要，不保存图像。连续完全相同画面达到 0.5 秒即 WARN，并报告最长重复持续时间；文件检查采用同一逻辑，能发现整段中间出现的局部冻结。正常静止场景也可能命中，因此名称是“疑似冻结/静态场景”，需要人工确认。近似冻结（像素仍有噪声变化）、失焦和曝光问题仍需人工检查。时间戳冻结、重复、倒退、NaN、未来或过期为 FAIL；在线异常后保留最高已接受时间戳，不因清空同步缓存而接受更老消息。文件检查先检查原顺序，不能通过排序去重掩盖倒退。

保存文件中的合法源帧复用必须同时复用原图像；同一相机相同源时间戳对应不同像素时判 FAIL，不能作为正常复用放过。

**LeRobot 转换后全量一致性检查（完全离线）：** 使用独立 LeRobot 环境，不装进 ROS Python。默认要求正式采集来源，模拟转换验证才加 `--allow-preview`。示例路径与 4.8 对应：

```bash
python3 scripts/run.py exec -- env HF_HUB_OFFLINE=1 \
  PYTHONPATH=/workspace/Pika_data/pika_ros/src/pika_bimanual \
  /workspace/Pika_data/.analysis/lerobot-venv/bin/python -m pika_bimanual.check lerobot \
  --config /workspace/Pika_data/.analysis/rig.local.yaml \
  --lerobot-dir /workspace/data/rig_acceptance_001_lerobot \
  --repo-id local/pika_bimanual \
  --report-dir /workspace/Pika_data/.analysis/check_lerobot_001
```

检查器强制 Hugging Face 离线模式，不上传或下载数据。必须保留 `pika_conversion.json` 及其中指向的原始 HDF5；缺失原文件时报告 FAIL，不能证明转换一致性。当前针对本项目导出的 v3 无损 image 数据集，不将任意外部视频数据集视为相同格式。

它会核对 v3/fps、相机集合/尺寸、14 维名称顺序与数据类型、原文件单位和配置、episode/frame 总数；重新按原始控制时间计算因果重采样索引，与 manifest 逐项核对；最后使用官方读取器遍历**全部帧和全部像素**，验证 state/action、三图、task、episode/frame/global index 及输出时间戳。状态/动作按导出的 float32 精度比较，图像按 RGB HWC → CHW/255 后以 1e-6 容差比较。输出 PASS 代表转换一致；来源为 preview/synthetic 时仍保留 WARN。全量比较比首/中/尾抽查更慢，报告记录已验证帧数和首个失败位置，不修改原始或转换后数据。

质量建议阈值默认 `--min-hz 27 --max-gap 0.1`，同步/时效硬阈值来自 rig 配置。WARN 需要逐项复核后再决定是否用于训练；FAIL 不进入 LeRobot 转换。报告目录已存在时换新编号，不自动覆盖旧证据。文件或配置读取失败也尽可能输出 FAIL 报告；命令参数错误、输出目录不可写时终端会直接报错。

### 6. 旧入口兼容与常见问题

- `teleop` / `collect` / `capture` 仍是原装 Piper 夹爪的旧方案，未切换到新硬件；不要与 `bimanual` 并行启动。
- `hardware_calibrated` 或 D435 序列号报错：填真实标定/序列号，不使用虚构值绕过。
- `/pika/status` 提示 missing/stale：先检查报错 topic；示教模式还需开启 `/pika/teleop_enable` 才有 IK 目标。
- 三相机配置缺全局图：接入 D435 或明确改为两相机配置；不会静默降级。
- 输出未开放但想离线录制：只有测试时添加 `--preview-recording`；产物会标为预览。
- 进程中断后出现 `.partial`：保留作诊断，工具不会覆盖或当作完整 episode。
- 修改配置/launch/安装列表后重新 overlay；日常直接修改 Python 源码可由 symlink-install 生效。

离线验证包括 ROS 模拟采集/回放、实际 Pinocchio/SciPy 求解、三相机错相时间戳、遥操暂停/心跳/重设基线、损坏文件拒绝、伪串口以及真实 LeRobot 写入后重读。运行基础回归用 `bimanual-test`；其中 LeRobot 测试在 ROS 环境跳过，在上述独立环境运行 `python -m pytest -q /workspace/Pika_data/pika_ros/src/pika_bimanual/test/test_audit.py`（同时设置上面的 PYTHONPATH）。日志保存在项目 `.analysis/bimanual-audit-test.log` 与 `.analysis/lerobot-roundtrip-test.log`。未启动真实 CAN、串口、相机或机械臂，未使用真实模型权重。

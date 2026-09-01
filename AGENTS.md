# Pika_data Project Context

这是 Codex 处理本项目时必须首先阅读的长期项目上下文文件。它同时是新窗口快速恢复指南和工程操作规范。

- 如果代码与本文件冲突，以当前代码为准。
- 如果硬件实际行为与文档冲突，以安全的实机验证和官方最新说明为准。
- 不要根据旧手册自行猜测新版硬件行为；证据不足时明确标记 `UNKNOWN`。

## 1. 项目主线与当前阶段

项目目标：

```text
Pika Sense + Pika Station Pro
  -> 空间定位 / 手柄状态
  -> ROS2 Humble 遥操作
  -> AgileX Piper + 原装夹爪
  -> 机器人示范数据采集
  -> VLA / imitation learning
  -> 模型部署
  -> ROS1 / ROS2 adapter
```

Docker 基础环境已基本完成。当前核心目标已经转为：

```text
真实硬件接入 -> 定位校准 -> Piper 遥操 -> 数据采集 -> VLA 训练和部署
```

用户问“下一步怎么做”时，默认沿这条主线继续，除非用户明确切换任务。

## 2. Host / Container 架构边界

Host 是 Ubuntu 20.04，负责：

- Linux kernel、Docker daemon、USB、`/dev`、udev
- SocketCAN、USB-CAN、CAN interface 创建/命名/bitrate
- RealSense/Sense/Vive USB 权限、X11 和真实硬件

Container 是 Ubuntu 22.04 + ROS2 Humble，负责：

- ROS2、Pika runtime、`pika_locator`、libsurvive
- librealsense userspace、pyAgxArm、teleop、data capture

不要把 Host 的 kernel、udev、CAN 职责塞进容器。不要因为容器是 root，就在容器内执行 Host udev/CAN 初始化脚本。仓库中的相关脚本带有历史机器的 USB 拓扑假设。

## 3. 关键目录

```text
Pika_data/
├── docker/                 # Dockerfile、Compose、entrypoint
├── scripts/run.py          # 统一运行入口
├── third_party/            # 第三方版本记录
├── pika_ros/               # ROS2 workspace submodule
├── pyAgxArm/               # AgileX Python SDK submodule
├── README.md
├── .gitmodules
└── AGENTS.md
```

- `third_party/manifest.yaml`：第三方依赖、commit 和嵌套关系记录。
- `.analysis/`：Git ignored 的只读分析产物，不是正式运行源码。
- 处理具体函数、topic、参数前，仍需读取当前源码，不能只依赖本文件。

## 4. Docker 当前状态

已完成并验证：

- Ubuntu 22.04 + ROS2 Humble 镜像构建
- librealsense 2.55.1
- 官方 `install.zip` vendor underlay
- vendor 旧路径、Python shebang、ELF RUNPATH 处理
- Host source bind mount 和本地 colcon overlay
- 11 个 ROS package 编译成功
- doctor、ShellCheck、yamllint、Compose config 检查

vendor underlay 位于 `/opt/pika/vendor/install`。环境叠加顺序是：

```text
/opt/ros/humble
  -> vendor underlay
  -> local pika_ros/install
  -> bind-mounted pyAgxArm
```

libsurvive 校准保存在 `~/.config/libsurvive`，已通过 Docker volume 持久化。不要随意执行 `docker compose down -v`，它可能删除定位校准数据。

### 已知 Docker 阻塞

当前镜像审阅发现 CasADi、Pinocchio 可能尚未作为 teleop runtime 正确安装；`arm_ik_pose_node.py` 依赖它们。因此“11 个 ROS package 编译成功”不等于“teleop 可以运行”。

启动 teleop 前先验证：

```text
python import casadi
python import pinocchio
arm_ik_pose_node.py runtime
```

优先做最小依赖修复，不要无理由大规模重建 Docker/vendor 方案。

## 5. ROS2 package 结构

源码 overlay 的 11 个 package：

- `agx_arm_ctrl`：ROS2 与 pyAgxArm 的驱动桥、反馈、控制和服务。
- `agx_arm_description`：Piper/Nero URDF、Xacro 和 mesh。
- `agx_arm_moveit`：MoveIt2 配置和轨迹控制门。
- `agx_arm_msgs`：机械臂、夹爪和灵巧手消息。
- `pika_remote_agx_arm`：Pika pose -> delta pose -> IK -> Piper command。
- `data_msgs`：采集、定位、gripper、instruction 等消息/服务。
- `data_tools`：采集、同步、HDF5、MCAP、回放、LeRobot 转换。
- `sensor_tools`：Sense、gripper、鱼眼相机和 RealSense 输入。
- `realsense2_camera`、`realsense2_camera_msgs`、`realsense2_description`。

vendor 提供 `pika_locator`、libsurvive、`survive-cli`。`pika_locator` 当前主要是预编译二进制，内部变换/滤波实现不能完整源码审计。

## 6. Pika Sense 链路

Sense serial 默认 460800 baud，主要输出：

- `/gripper/data`
- `/gripper/joint_state`

launch 可能对它们重映射或加命名空间。Sense 的 `Command` 字段可触发 teleop Trigger service 和 `/data_tools_dataCapture/capture_service`。

历史设备名包括 `/dev/ttyUSB50`、`60`、`61`、`70`，不能假设当前主机一致。实机接入时重新核对 `lsusb`、`/dev/ttyUSB*` 和 USB topology，再制定 Host udev 规则。

## 7. Station Pro / locator 链路

当前硬件是 **Pika Station Pro**：

```text
Station Pro -> Sense tracker -> libsurvive -> pika_locator -> PoseStamped
```

- 单手 pose：`/pika_pose`
- 双手 pose：`/pika_pose_l`、`/pika_pose_r`
- tracker code：`pika_locator/get_code.launch.py`
- 双手 code：环境变量 `pika_L_code`、`pika_R_code`
- 强制校准：`survive-cli --force-calibrate`
- 校准结果：`~/.config/libsurvive`

Pika Station Pro 的 channel 设置方式是 **UNKNOWN**。旧版手册的“不同频道”不能直接套用。除非官方、当前源码或安全实机验证给出明确证据，不要猜测 CAN、USB、SteamVR、libsurvive、自动频道或固定频道方案。

## 8. Piper 控制链路

核心 ROS 节点是 `AgxArmRosNode`。

反馈：

- `/feedback/joint_states`、`/feedback/tcp_pose`
- `/feedback/arm_status`、`/feedback/gripper_status`
- `/feedback/leader_joint_states`

控制：

- `/control/joint_states`
- `/control/move_j`、`/control/move_js`
- `/control/move_p`、`/control/move_l`、`/control/move_c`
- `/control/move_mit`

服务：

- `/enable_agx_arm`、`/control_enable`
- `/move_home`、`/emergency_stop`、`/exit_teach_mode`

主控制链：

```text
/control/joint_states
  -> AgxArmRosNode
  -> pyAgxArm.move_js()
  -> python-can -> SocketCAN -> USB-CAN -> Piper
```

pyAgxArm 公共接口中 joint 使用 rad、position 使用 m。Host SocketCAN 通常为 1 Mbps，但接口名和真实 bitrate 必须在 Host 确认。

## 9. 单臂 teleop 调用链

入口是 `teleop_single_piper.launch.py`：

```text
Station/Sense -> libsurvive -> pika_locator -> /pika_pose
  -> pub_delta_pose.py
     subscribes /pika_pose, /feedback/tcp_pose, /gripper/joint_state
     publishes /delta_pose
  -> arm_ik_pose_node.py
     subscribes /delta_pose, /feedback/joint_states
     uses Pinocchio + CasADi + IPOPT
     publishes /control/joint_states, /ik_fk_pose
  -> agx_arm_ctrl -> pyAgxArm -> SocketCAN -> Piper
```

安全事实：该 launch 当前默认 `auto_enable=true`，不能直接作为首次实机安全诊断入口。

### 当前夹爪缺口

Sense gripper -> Piper 原装夹爪没有完整接通。`pub_delta_pose.py` 中相关转换/发布代码被注释，IK 只输出 `joint1...joint6`。不能认为 Piper 原装夹爪已经能被 Sense 遥控。

## 10. 数据采集能力与格式

已有：`DataCapture`、`DataCaptureService`、`DataSync`、`data_to_hdf5.py`、`DataPublish`、MCAP、HDF5 和 LeRobot 2.1 转换。

可采集 RGB、depth、point cloud、joint state、end pose、locator pose、gripper、IMU、force、ndarray、lidar、base odometry、instruction 和 TF。

原始格式：

- RGB `.jpg`；Depth `.png`；Point cloud `.pcd`
- Joint/Pose/Gripper/IMU `.json`；Array `.npy`
- 使用 ROS header timestamp；最近邻同步默认 tolerance 约 30 ms
- 采集端保存各 topic 原生频率，不强制全部 topic 为同一 Hz

### 数据采集未完成项

1. 现有 YAML topic 与单 Sense + Piper 实际 topic 不完全匹配。
2. teleop-only sensor launch 不启动相机。
3. Piper 原装夹爪状态与现有 `data_msgs/Gripper` 配置不同。
4. Sense -> Piper gripper bridge 缺失。
5. dataset schema/version 和 episode metadata 尚未稳定。
6. LeRobot observation/action mapping 尚未最终审计。
7. **HIGH RISK：重复 episode index 时，DataCapture 可能递归删除旧 episode。正式采集前优先修复。**

## 11. 模型部署原则

训练数据当前来自 ROS2，但模型以后可部署到 ROS1。policy core 不应直接依赖 `rclpy` 或 `rospy`。

稳定定义 observation、action、坐标系、单位、timestamp、frequency 和 image preprocessing，推荐结构：

```text
policy/
ros1_adapter/
ros2_adapter/
```

## 12. 硬件接入默认安全顺序

1. Host USB inventory。
2. 只连接 Station Pro + Sense。
3. locator calibration。
4. Sense input validation。
5. Host SocketCAN 配置与只读检查。
6. Piper read-only feedback：`auto_enable=false`、`control_enabled=false`。
7. teleop dry run，只观察 pose、IK 和目标命令。
8. 低风险、小幅、低速真实运动。
9. 接通 gripper。
10. data capture。

验证坐标方向、TCP offset、joint limits、IK output、watchdog 和 physical emergency stop 前，不要开启真实运动。

## 13. 风险登记

HIGH：

- CasADi/Pinocchio runtime 未确认
- teleop `auto_enable=true`
- episode overwrite/delete
- Sense -> Piper gripper 缺失
- acquisition YAML mismatch

MEDIUM：

- command watchdog 缺失
- self-collision check disabled
- workspace guard 缺失
- udev rule 硬编码、CAN 命名不稳定
- 坐标系尚未实机验证

KNOWN BUG：双臂 Piper launch 中左右 `pub_delta_pose` 的 trigger service 配置有误。当前做单臂任务时不要顺手修改双臂代码，除非用户明确要求。

UNKNOWN：Pika Station Pro channel configuration。

## 14. Git / submodule 关系

- 顶层：branch `main`，origin `https://github.com/Jingxuan-Li-0921/Pika_data.git`
- `pika_ros`：branch `ros2`，基准 `9f469895bd816e408616ab5cbf5112ba3fd5191a`；origin 是用户 fork，upstream 是 AgileX 官方。
- `pyAgxArm`：branch `master`，基准 `2255d88e1fabdf20fcd1eccbc4312b4ce1cfd2d4`；origin 是用户 fork，upstream 是 AgileX 官方。
- `agx_arm_ros`：特殊嵌套仓库，branch `ros2`，commit `77882f4305c5e169b4542b408ac9f6755bdfa7c8`。

不要破坏 `PikaAnyArm`、`data_msgs`、`data_tools`、`agx_arm_ros`、`agx_arm_urdf` 的版本关系。不要随意删除 `.git`、重新初始化 submodule、clean 或 reset。

### Git 操作规则

- 修改前运行 `git status`，修改后运行 `git diff`。
- 不自动执行 `git reset --hard`、`git clean -fd`、`git checkout .`、`git restore .` 或 `git stash`。
- 不自动 push；需要 commit 时先说明改动。
- 修改 `pika_ros` 时，源码 commit 属于 `pika_ros` 自己的仓库；之后才在顶层更新 submodule gitlink。
- 不要把 `pika_ros` 内部源码作为普通文件直接提交到顶层仓库。

## 15. 硬件危险操作规则

未经用户明确授权，禁止：

- enable Piper 或发送 `move_j/move_js/move_p/move_l`
- 发送原始 CAN frame
- 执行 emergency-stop reset
- 修改 firmware、Station 参数或 factory reset
- 修改 Host udev/CAN 状态

若用户明确要求真实运动，先检查 arm state、control gate、speed、workspace、physical emergency stop 和 requested trajectory，再以最小运动量验证。

## 16. 新窗口工作流程

1. 首先完整阅读本文件。
2. 运行 `git status`，保护用户已有改动。
3. 根据任务读取相关当前源码，不重复无目的扫描整个仓库。
4. 已由本文件确认的架构可直接复用；具体函数、topic、参数和 Git 状态必须以当前代码复核。

## 17. 默认后续优先级

1. 验证并最小补齐 CasADi/Pinocchio runtime。
2. 建立 Piper read-only/safe diagnostic launch。
3. 配置当前 Host 的 USB/udev/CAN。
4. Station Pro + Sense 校准并验证 `/pika_pose`。
5. Piper feedback only；随后 teleop dry run。
6. 增加 watchdog、speed limit、workspace guard。
7. 开启低风险真实遥操作。
8. 实现 Sense -> Piper 原装夹爪。
9. 修正单臂采集 YAML 和 episode overwrite。
10. 短 episode 完成 capture -> sync -> HDF5 -> playback 验收。
11. 正式数据采集、VLA training、ROS1/ROS2 model deployment。

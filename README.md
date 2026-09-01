# Pika Data Docker Environment

本工程在 Ubuntu 20.04 宿主机上，通过 Docker 提供 Pika 官方软件所需的 Ubuntu 22.04 与 ROS 2 Humble 开发、编译和运行环境。

## 当前状态

当前工程已经包含：

- 基于 Ubuntu 22.04 / ROS 2 Humble 的 Docker image
- Docker Compose 开发环境
- Pika 源码的宿主机 bind mount
- 预编译 Pika vendor underlay
- 本地 colcon overlay 与独立的 build/install/log volumes
- librealsense 2.55.1
- 宿主机入口脚本 `scripts/run.py`
- 11 个 ROS package 的本地编译配置与已通过的编译结果

已验证容器能够识别 Pika Sense 的 RealSense D405、鱼眼相机、串口和定位标签。
普通容器启动不会修改宿主机 udev、CAN 或网络状态；只有显式运行
`setup-device` 时，才会在确认设备身份后通过 `sudo` 安装生成的 Pika udev 规则。

## 环境职责

宿主机负责：

- Docker daemon
- USB 设备与 udev
- SocketCAN 与 USB-CAN
- X11
- 真实硬件连接

Container 负责：

- Ubuntu 22.04
- ROS 2 Humble
- Pika runtime
- librealsense
- Python 环境（当前镜像使用系统 Python 3；如需 Conda，应在容器侧管理）
- ROS workspace、vendor underlay 与 local colcon overlay

## 获取工程

本仓库使用 submodule 管理 `pika_ros` 和 `pyAgxArm`：

```bash
git clone --recursive <YOUR_PIKA_DATA_REPOSITORY>
cd Pika_data
git submodule update --init --recursive
```

`pika_ros` 自己管理其内部 submodule 和嵌套依赖；顶层仓库不会重复跟踪这些内部源码。

## 使用方式

在工程根目录执行：

```bash
cd Pika_data
python3 scripts/run.py
```

无参数运行等价于 `shell --hardware`，会启动一个可访问 USB 等硬件设备的临时
交互式容器：

```bash
cd ~/project/Pika_data
python3 scripts/run.py
```

`run.py` 还支持以下显式子命令：

```bash
# 构建镜像；可附加 --pull、--no-cache 或 --progress
python3 scripts/run.py build

# 打开容器 shell；--build 表示启动前构建镜像
python3 scripts/run.py shell
python3 scripts/run.py shell --build

# 连接 Watchman、RealSense 等 USB 硬件时使用；不要只映射单个 USB 设备号
python3 scripts/run.py shell --hardware

# 在临时容器中执行任意命令或 ros2 命令
python3 scripts/run.py exec -- <command>
python3 scripts/run.py ros2 -- <ros2-arguments>

# 在可访问实时 USB 设备树的临时容器中执行命令
python3 scripts/run.py exec --hardware -- survive-cli --force-calibrate

# 交互识别左右 Sense，并由 run.py 在宿主机安装和验证稳定设备名
python3 scripts/run.py setup-device

# 构建本地 ROS overlay；默认执行 colcon build --symlink-install
python3 scripts/run.py overlay

# 检查 ROS、vendor、overlay 以及 Python 依赖
python3 scripts/run.py doctor

# 双 Sense + 双 Piper：只计算 IK，绝不发布真实机械臂命令
python3 scripts/run.py teleop-dry-run

# 启动带命令守卫的双臂栈；机械臂、驱动控制门和守卫仍默认关闭
python3 scripts/run.py teleop

# 启动同一安全遥操栈和按服务控制的数据采集
python3 scripts/run.py collect \
  --dataset-dir /workspace/data/dual_pika_piper \
  --episode-index 0 \
  --instructions '["task description"]'

# 启动、查看日志和停止 Compose service
python3 scripts/run.py up --detach
python3 scripts/run.py logs --follow
python3 scripts/run.py down
```

三个双臂入口都会先在宿主机检查 `can_left`、`can_right` 是否存在、处于 UP
状态且波特率为 1 Mbps，并检查左右 Sense 的稳定设备别名。预检失败时不会启动
容器。`teleop` 和 `collect` 不会自动使能 Piper，也不会自动打开控制门；首次真实
运动必须在急停、工作空间、坐标方向和初始目标误差均确认后单独授权。

`source/install.zip` 和 `source/librealsense-2.55.1.zip` 只在构建镜像时由
Dockerfile 解压。日常进入容器不需要、也不应再次手动解压。Pika 的预编译
underlay 位于 `/opt/pika/vendor/install` 并由入口脚本自动加载；
`pika_ros/install` 只用于本地 `colcon` overlay，并由 Compose named volume 持久化。

libsurvive 的配置和标定数据保存在独立的 `pika_config` named volume 中，因此
使用 `run --rm` 退出临时容器后仍会保留。只有显式执行 `docker compose down -v`
或删除该 volume 才会清除这些数据。

需要彻底重建镜像时，使用现有 `build` 子命令的 `--no-cache` 参数：

```bash
python3 scripts/run.py build --no-cache
```

## 目录结构

```text
Pika_data/
├── docker/       # Dockerfile、Compose 配置与容器入口
├── scripts/      # 宿主机操作入口
├── third_party/  # 固定版本与依赖清单
├── pika_ros/     # 顶层 Git submodule；ROS 2 workspace
└── pyAgxArm/     # 顶层 Git submodule；AgileX Python SDK
```

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

当前尚未进行真实 Pika Sense、RealSense、Piper 或 USB-CAN 硬件验证。Compose 配置不会自动修改宿主机 udev、CAN 或网络状态，硬件设备需要在实际测试时显式传入。

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

无参数运行等价于 `shell`，会启动一个临时交互式容器。`run.py` 当前支持以下子命令：

```bash
# 构建镜像；可附加 --pull、--no-cache 或 --progress
python3 scripts/run.py build

# 打开容器 shell；--build 表示启动前构建镜像
python3 scripts/run.py shell
python3 scripts/run.py shell --build

# 在临时容器中执行任意命令或 ros2 命令
python3 scripts/run.py exec -- <command>
python3 scripts/run.py ros2 -- <ros2-arguments>

# 构建本地 ROS overlay；默认执行 colcon build --symlink-install
python3 scripts/run.py overlay

# 检查 ROS、vendor、overlay 以及 Python 依赖
python3 scripts/run.py doctor

# 启动、查看日志和停止 Compose service
python3 scripts/run.py up --detach
python3 scripts/run.py logs --follow
python3 scripts/run.py down
```

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

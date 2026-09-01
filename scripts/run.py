#!/usr/bin/env python3
"""Host-side wrapper for the Pika Docker/Compose development image.

ROS and colcon work stays in the container. The explicit ``setup-device``
workflow is the only path that installs generated Pika udev rules on the host.
"""

from __future__ import annotations

import argparse
from contextlib import contextmanager
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import time
from typing import Iterator, Sequence


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
COMPOSE_FILE = REPOSITORY_ROOT / "docker" / "docker-compose.yaml"
HARDWARE_COMPOSE_FILE = REPOSITORY_ROOT / "docker" / "docker-compose.hardware.yaml"
SERVICE = os.environ.get("PIKA_COMPOSE_SERVICE", "pika")
X11_CONTAINER_IDENTITY = "SI:localuser:root"
DEVICE_SETUP_DIR = REPOSITORY_ROOT / ".analysis" / "device_setup"
DEVICE_SETUP_CONTAINER_DIR = "/workspace/Pika_data/.analysis/device_setup"


def compose_command() -> list[str]:
    docker = shutil.which("docker")
    if docker:
        probe = subprocess.run(
            [docker, "compose", "version"],
            cwd=REPOSITORY_ROOT,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=False,
        )
        if probe.returncode == 0:
            return [docker, "compose"]

    legacy_compose = shutil.which("docker-compose")
    if legacy_compose:
        return [legacy_compose]

    raise RuntimeError("Docker Compose is not available (tried `docker compose` and `docker-compose`).")


def compose_base(hardware: bool = False) -> list[str]:
    if not COMPOSE_FILE.is_file():
        raise RuntimeError(f"Compose file not found: {COMPOSE_FILE}")
    command = compose_command() + ["-f", str(COMPOSE_FILE)]
    if hardware:
        if not HARDWARE_COMPOSE_FILE.is_file():
            raise RuntimeError(f"Hardware Compose file not found: {HARDWARE_COMPOSE_FILE}")
        command.extend(["-f", str(HARDWARE_COMPOSE_FILE)])
    return command


@contextmanager
def container_x11_access(enabled: bool) -> Iterator[None]:
    """Temporarily allow the root user in the local container to use X11."""
    display = os.environ.get("DISPLAY", "").strip()
    if not enabled or not display:
        if enabled and not display:
            print(
                "[pika-run] DISPLAY is unset; starting without X11 GUI access.",
                file=sys.stderr,
            )
        yield
        return

    xhost = shutil.which("xhost")
    if not xhost:
        raise RuntimeError(
            "DISPLAY is set but `xhost` is unavailable on the host "
            "(install the host package `x11-xserver-utils`)"
        )

    grant = subprocess.run(
        [xhost, f"+{X11_CONTAINER_IDENTITY}"],
        cwd=REPOSITORY_ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    if grant.returncode != 0:
        detail = (grant.stderr or grant.stdout).strip()
        raise RuntimeError(f"failed to grant temporary X11 access: {detail}")

    print(f"[pika-run] Granted temporary X11 access on DISPLAY={display}.")
    try:
        yield
    finally:
        revoke = subprocess.run(
            [xhost, f"-{X11_CONTAINER_IDENTITY}"],
            cwd=REPOSITORY_ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        if revoke.returncode == 0:
            print("[pika-run] Revoked temporary X11 access.")
        else:
            detail = (revoke.stderr or revoke.stdout).strip()
            print(
                f"[pika-run] warning: failed to revoke X11 access: {detail}",
                file=sys.stderr,
            )


def run_compose(
    arguments: Sequence[str], hardware: bool = False, x11: bool = False
) -> int:
    command = compose_base(hardware) + list(arguments)
    with container_x11_access(x11):
        completed = subprocess.run(command, cwd=REPOSITORY_ROOT, check=False)
    return completed.returncode


def strip_separator(arguments: Sequence[str]) -> list[str]:
    values = list(arguments)
    if values[:1] == ["--"]:
        return values[1:]
    return values


def add_run_prefix(build: bool) -> list[str]:
    command = ["run", "--rm"]
    if build:
        command.append("--build")
    command.append(SERVICE)
    return command


def command_build(args: argparse.Namespace) -> int:
    docker_args: list[str] = []
    if args.progress:
        docker_args.extend(["--progress", args.progress])
    docker_args.append("build")
    if args.pull:
        docker_args.append("--pull")
    if args.no_cache:
        docker_args.append("--no-cache")
    return run_compose(docker_args)


def command_shell(args: argparse.Namespace) -> int:
    command = add_run_prefix(args.build) + ["bash"]
    command.extend(strip_separator(args.command))
    return run_compose(command, hardware=args.hardware, x11=True)


def command_exec(args: argparse.Namespace) -> int:
    command = add_run_prefix(args.build) + strip_separator(args.command)
    if len(command) == len(add_run_prefix(args.build)):
        raise RuntimeError("exec requires a command")
    return run_compose(command, hardware=args.hardware)


def command_ros2(args: argparse.Namespace) -> int:
    command = add_run_prefix(args.build) + ["ros2"] + strip_separator(args.command)
    return run_compose(command, hardware=args.hardware)


def command_overlay(args: argparse.Namespace) -> int:
    colcon_args = strip_separator(args.colcon_args)
    if not colcon_args:
        colcon_args = ["build", "--symlink-install"]
    command = add_run_prefix(args.build) + ["colcon"] + colcon_args
    return run_compose(command, hardware=args.hardware)


def command_doctor(args: argparse.Namespace) -> int:
    del args
    check_script = (
        "set -eu; "
        "printf 'ROS_DISTRO=%s\\n' \"$ROS_DISTRO\"; "
        "printf 'ros2=%s\\n' \"$(command -v ros2)\"; "
        "printf 'colcon=%s\\n' \"$(command -v colcon)\"; "
        "test -f \"$PIKA_VENDOR_PREFIX/setup.bash\"; "
        "printf 'vendor=%s\\n' \"$PIKA_VENDOR_PREFIX\"; "
        "if test -f \"$PIKA_WS/install/local_setup.bash\"; then "
        "printf 'overlay=%s\\n' \"$PIKA_WS/install\"; "
        "else printf 'overlay=not-built\\n'; fi; "
        "python3 -c 'import pyAgxArm, can, pinocchio, scipy; "
        "print(\"pyAgxArm=ok\"); print(\"python-can=ok\"); "
        "print(\"pinocchio=ok\"); print(\"scipy=ok\")'"
    )
    return run_compose(add_run_prefix(False) + ["bash", "-c", check_script])


def command_setup_device(args: argparse.Namespace) -> int:
    """Discover Pika devices in the container and install rules on the host."""
    DEVICE_SETUP_DIR.mkdir(parents=True, exist_ok=True)
    discover = add_run_prefix(args.build) + [
        "python3",
        "scripts/setup_device.py",
        "--host-managed",
        "--output-dir",
        DEVICE_SETUP_CONTAINER_DIR,
    ]
    status = run_compose(discover, hardware=True)
    if status != 0:
        return status

    manifest_path = DEVICE_SETUP_DIR / "manifest.json"
    try:
        manifest = json.loads(manifest_path.read_text())
    except (OSError, json.JSONDecodeError) as error:
        raise RuntimeError(f"invalid device setup manifest: {error}") from error
    if manifest.get("version") != 1:
        raise RuntimeError("unsupported device setup manifest version")

    sudo = shutil.which("sudo")
    udevadm = shutil.which("udevadm")
    if not sudo or not udevadm:
        raise RuntimeError("host commands `sudo` and `udevadm` are required")

    rule_names = manifest.get("rules")
    if not isinstance(rule_names, list) or not rule_names:
        raise RuntimeError("device setup did not generate any udev rules")
    for filename in rule_names:
        if not isinstance(filename, str) or not re.fullmatch(
            r"99-pika-[a-z-]+\.rules", filename
        ):
            raise RuntimeError(f"unsafe udev rule filename in manifest: {filename!r}")
        source = DEVICE_SETUP_DIR / filename
        if not source.is_file():
            raise RuntimeError(f"generated udev rule is missing: {source}")
        completed = subprocess.run(
            [sudo, "install", "-m", "0644", str(source), f"/etc/udev/rules.d/{filename}"],
            cwd=REPOSITORY_ROOT,
            check=False,
        )
        if completed.returncode != 0:
            return completed.returncode

    for command in (
        [sudo, udevadm, "control", "--reload-rules"],
        [sudo, udevadm, "trigger", "--subsystem-match=tty", "--action=add"],
        [sudo, udevadm, "trigger", "--subsystem-match=video4linux", "--action=add"],
        [sudo, udevadm, "settle"],
    ):
        completed = subprocess.run(command, cwd=REPOSITORY_ROOT, check=False)
        if completed.returncode != 0:
            return completed.returncode

    print("[pika-run] Host udev rules installed and reloaded.")
    input(
        "请把左右两个 Sense 都重新插回绑定时各自的 USB 口，然后按回车检查 / "
        "Reconnect both Sense devices to their assigned USB ports, then press Enter: "
    )
    expected = [Path(value) for value in manifest.get("expected_devices", [])]
    deadline = time.monotonic() + 15
    missing = expected
    while time.monotonic() < deadline:
        missing = [path for path in expected if not path.exists()]
        if not missing:
            break
        time.sleep(1)
    if missing:
        print(
            "[pika-run] udev rules are installed, but these device aliases are still missing: "
            + ", ".join(str(path) for path in missing),
            file=sys.stderr,
        )
        print("[pika-run] Check that both devices use the same USB ports selected during binding.")
        return 1

    print("[pika-run] Device binding verified: " + ", ".join(str(path) for path in expected))
    print(f"[pika-run] Generated launcher: {DEVICE_SETUP_DIR}")
    return 0


def command_up(args: argparse.Namespace) -> int:
    command = ["up"]
    if args.build:
        command.append("--build")
    if args.detach:
        command.append("--detach")
    command.append(SERVICE)
    return run_compose(command)


def command_down(args: argparse.Namespace) -> int:
    del args
    return run_compose(["down"])


def command_logs(args: argparse.Namespace) -> int:
    command = ["logs"]
    if args.follow:
        command.append("--follow")
    command.append(SERVICE)
    return run_compose(command)


def validate_dual_piper_host(require_cameras: bool) -> None:
    """Fail closed when the expected host-side CAN/device aliases are absent."""
    ip_command = shutil.which("ip")
    if not ip_command:
        raise RuntimeError("host command `ip` is required for SocketCAN checks")
    for interface in ("can_left", "can_right"):
        result = subprocess.run(
            [ip_command, "-details", "link", "show", interface],
            cwd=REPOSITORY_ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        output = result.stdout
        if result.returncode != 0:
            raise RuntimeError(f"required SocketCAN interface is missing: {interface}")
        if not re.search(r"\bstate UP\b", output):
            raise RuntimeError(f"SocketCAN interface is not UP: {interface}")
        if not re.search(r"\bbitrate 1000000\b", output):
            raise RuntimeError(f"SocketCAN interface is not configured at 1 Mbps: {interface}")

    # An UP/ERROR-ACTIVE SocketCAN controller can still have no powered Piper
    # connected. Piper feedback is continuous, so require both RX counters to
    # advance before starting any ROS hardware stack.
    rx_counters: dict[str, int] = {}
    for interface in ("can_left", "can_right"):
        counter_path = Path(f"/sys/class/net/{interface}/statistics/rx_packets")
        try:
            rx_counters[interface] = int(counter_path.read_text().strip())
        except (OSError, ValueError) as error:
            raise RuntimeError(
                f"cannot read SocketCAN RX counter for {interface}: {error}"
            ) from error
    time.sleep(0.25)
    silent_interfaces = []
    for interface, previous_count in rx_counters.items():
        counter_path = Path(f"/sys/class/net/{interface}/statistics/rx_packets")
        try:
            current_count = int(counter_path.read_text().strip())
        except (OSError, ValueError) as error:
            raise RuntimeError(
                f"cannot re-read SocketCAN RX counter for {interface}: {error}"
            ) from error
        if current_count <= previous_count:
            silent_interfaces.append(interface)
    if silent_interfaces:
        raise RuntimeError(
            "no live Piper feedback frames on: " + ", ".join(silent_interfaces)
        )

    expected_devices = [Path("/dev/ttyUSB50"), Path("/dev/ttyUSB51")]
    if require_cameras:
        expected_devices.extend((Path("/dev/video50"), Path("/dev/video51")))
    missing = [str(path) for path in expected_devices if not path.exists()]
    if missing:
        raise RuntimeError("required Pika device aliases are missing: " + ", ".join(missing))
    print("[pika-run] Host CAN and Pika device preflight passed.")


def command_teleop_launch(args: argparse.Namespace) -> int:
    require_cameras = args.profile != "dry-run"
    validate_dual_piper_host(require_cameras=require_cameras)
    launch_file = {
        "dry-run": "teleop_double_piper_dry_run.launch.py",
        "official": "teleop_double_piper_runtime.launch.py",
        "collect": "collect_double_piper.launch.py",
    }[args.profile]
    command = add_run_prefix(args.build) + [
        "ros2",
        "launch",
        "pika_remote_agx_arm",
        launch_file,
    ]
    if args.profile == "collect":
        command.extend(
            [
                f"dataset_dir:={args.dataset_dir}",
                f"episode_index:={args.episode_index}",
                f"instructions:={args.instructions}",
            ]
        )
    return run_compose(command, hardware=True)


def command_capture(args: argparse.Namespace) -> int:
    command = add_run_prefix(args.build) + [
        "ros2",
        "launch",
        "data_tools",
        "run_dual_pika_piper_capture.launch.py",
        f"dataset_dir:={args.dataset_dir}",
        f"episode_index:={args.episode_index}",
        f"instructions:={args.instructions}",
    ]
    return run_compose(command)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Run Pika ROS2 commands in the Ubuntu 22.04/Humble container."
    )
    subparsers = parser.add_subparsers(dest="subcommand")

    build = subparsers.add_parser("build", help="Build the Docker image.")
    build.add_argument("--pull", action="store_true", help="Pull the base image first.")
    build.add_argument("--no-cache", action="store_true", help="Disable Docker build cache.")
    build.add_argument("--progress", choices=("auto", "plain", "tty"))
    build.set_defaults(handler=command_build)

    shell = subparsers.add_parser("shell", help="Open an interactive container shell.")
    shell.add_argument("--build", action="store_true", help="Build the image before starting.")
    shell.add_argument("--hardware", action="store_true", help="Enable live USB/device access.")
    shell.add_argument("command", nargs=argparse.REMAINDER, help="Optional bash arguments.")
    shell.set_defaults(handler=command_shell)

    execute = subparsers.add_parser("exec", help="Run an arbitrary command in a fresh container.")
    execute.add_argument("--build", action="store_true", help="Build the image before starting.")
    execute.add_argument("--hardware", action="store_true", help="Enable live USB/device access.")
    execute.add_argument("command", nargs=argparse.REMAINDER)
    execute.set_defaults(handler=command_exec)

    ros2 = subparsers.add_parser("ros2", help="Run `ros2 ...` in the container.")
    ros2.add_argument("--build", action="store_true", help="Build the image before starting.")
    ros2.add_argument("--hardware", action="store_true", help="Enable live USB/device access.")
    ros2.add_argument("command", nargs=argparse.REMAINDER)
    ros2.set_defaults(handler=command_ros2)

    overlay = subparsers.add_parser("overlay", help="Build the host-source ROS overlay with colcon.")
    overlay.add_argument("--build", action="store_true", help="Build the image before starting.")
    overlay.add_argument("--hardware", action="store_true", help="Enable live USB/device access.")
    overlay.add_argument("colcon_args", nargs=argparse.REMAINDER)
    overlay.set_defaults(handler=command_overlay)

    doctor = subparsers.add_parser("doctor", help="Check ROS, vendor, overlay, and Python imports.")
    doctor.set_defaults(handler=command_doctor)

    setup_device = subparsers.add_parser(
        "setup-device",
        help="Interactively bind Pika devices and install host udev rules.",
    )
    setup_device.add_argument(
        "--build", action="store_true", help="Build the image before device discovery."
    )
    setup_device.set_defaults(handler=command_setup_device)

    up = subparsers.add_parser("up", help="Start the Compose service.")
    up.add_argument("--build", action="store_true", help="Build the image before starting.")
    up.add_argument("--detach", action="store_true", help="Run in the background.")
    up.set_defaults(handler=command_up)

    down = subparsers.add_parser("down", help="Stop the Compose project.")
    down.set_defaults(handler=command_down)

    logs = subparsers.add_parser("logs", help="Show Compose service logs.")
    logs.add_argument("--follow", action="store_true")
    logs.set_defaults(handler=command_logs)

    for command_name, profile, help_text in (
        ("teleop-dry-run", "dry-run", "Run dual-Sense IK with arm command topics isolated."),
        ("teleop", "official", "Start the official direct dual-Piper teleoperation path."),
        ("collect", "collect", "Start the guarded teleoperation and capture stack."),
    ):
        command_parser = subparsers.add_parser(command_name, help=help_text)
        command_parser.add_argument("--build", action="store_true")
        command_parser.set_defaults(handler=command_teleop_launch, profile=profile)
        if profile == "collect":
            command_parser.add_argument(
                "--dataset-dir", default="/workspace/data/dual_pika_piper"
            )
            command_parser.add_argument("--episode-index", type=int, default=0)
            command_parser.add_argument("--instructions", default="[null]")

    capture = subparsers.add_parser(
        "capture", help="Start only the dual-Pika/Piper capture service."
    )
    capture.add_argument("--build", action="store_true")
    capture.add_argument("--dataset-dir", default="/workspace/data/dual_pika_piper")
    capture.add_argument("--episode-index", type=int, default=0)
    capture.add_argument("--instructions", default="[null]")
    capture.set_defaults(handler=command_capture)

    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    arguments = list(sys.argv[1:] if argv is None else argv)
    # Pika is a hardware workspace, so the shortest invocation opens an
    # interactive shell with live USB/device access enabled.
    if not arguments:
        arguments = ["shell", "--hardware"]
    parsed = parser.parse_args(arguments)
    try:
        return parsed.handler(parsed)
    except (OSError, RuntimeError) as error:
        print(f"run.py: error: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())

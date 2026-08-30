#!/usr/bin/env python3
"""Small host-side wrapper for the Pika Docker/Compose development image.

The wrapper intentionally delegates all ROS and colcon work to the container.
It does not configure CAN, USB permissions, udev rules, or host ROS packages.
"""

from __future__ import annotations

import argparse
import os
from pathlib import Path
import shutil
import subprocess
import sys
from typing import Sequence


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
COMPOSE_FILE = REPOSITORY_ROOT / "docker" / "docker-compose.yaml"
SERVICE = os.environ.get("PIKA_COMPOSE_SERVICE", "pika")


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


def compose_base() -> list[str]:
    if not COMPOSE_FILE.is_file():
        raise RuntimeError(f"Compose file not found: {COMPOSE_FILE}")
    return compose_command() + ["-f", str(COMPOSE_FILE)]


def run_compose(arguments: Sequence[str]) -> int:
    command = compose_base() + list(arguments)
    completed = subprocess.run(command, cwd=REPOSITORY_ROOT, check=False)
    return completed.returncode


def strip_separator(arguments: Sequence[str]) -> list[str]:
    values = list(arguments)
    if values[:1] == ["--"]:
        return values[1:]
    return values


def add_run_prefix(build: bool) -> list[str]:
    return ["run", "--rm"] + (["--build"] if build else []) + [SERVICE]


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
    return run_compose(command)


def command_exec(args: argparse.Namespace) -> int:
    command = add_run_prefix(args.build) + strip_separator(args.command)
    if len(command) == len(add_run_prefix(args.build)):
        raise RuntimeError("exec requires a command")
    return run_compose(command)


def command_ros2(args: argparse.Namespace) -> int:
    command = add_run_prefix(args.build) + ["ros2"] + strip_separator(args.command)
    return run_compose(command)


def command_overlay(args: argparse.Namespace) -> int:
    colcon_args = strip_separator(args.colcon_args)
    if not colcon_args:
        colcon_args = ["build", "--symlink-install"]
    command = add_run_prefix(args.build) + ["colcon"] + colcon_args
    return run_compose(command)


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
        "python3 -c 'import pyAgxArm, can; print(\"pyAgxArm=ok\"); print(\"python-can=ok\")'"
    )
    return run_compose(add_run_prefix(False) + ["bash", "-c", check_script])


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
    shell.add_argument("command", nargs=argparse.REMAINDER, help="Optional bash arguments.")
    shell.set_defaults(handler=command_shell)

    execute = subparsers.add_parser("exec", help="Run an arbitrary command in a fresh container.")
    execute.add_argument("--build", action="store_true", help="Build the image before starting.")
    execute.add_argument("command", nargs=argparse.REMAINDER)
    execute.set_defaults(handler=command_exec)

    ros2 = subparsers.add_parser("ros2", help="Run `ros2 ...` in the container.")
    ros2.add_argument("--build", action="store_true", help="Build the image before starting.")
    ros2.add_argument("command", nargs=argparse.REMAINDER)
    ros2.set_defaults(handler=command_ros2)

    overlay = subparsers.add_parser("overlay", help="Build the host-source ROS overlay with colcon.")
    overlay.add_argument("--build", action="store_true", help="Build the image before starting.")
    overlay.add_argument("colcon_args", nargs=argparse.REMAINDER)
    overlay.set_defaults(handler=command_overlay)

    doctor = subparsers.add_parser("doctor", help="Check ROS, vendor, overlay, and Python imports.")
    doctor.set_defaults(handler=command_doctor)

    up = subparsers.add_parser("up", help="Start the Compose service.")
    up.add_argument("--build", action="store_true", help="Build the image before starting.")
    up.add_argument("--detach", action="store_true", help="Run in the background.")
    up.set_defaults(handler=command_up)

    down = subparsers.add_parser("down", help="Stop the Compose project.")
    down.set_defaults(handler=command_down)

    logs = subparsers.add_parser("logs", help="Show Compose service logs.")
    logs.add_argument("--follow", action="store_true")
    logs.set_defaults(handler=command_logs)

    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    arguments = list(sys.argv[1:] if argv is None else argv)
    # A no-argument invocation is the convenient equivalent of `shell`.
    if not arguments:
        arguments = ["shell"]
    parsed = parser.parse_args(arguments)
    try:
        return parsed.handler(parsed)
    except (OSError, RuntimeError) as error:
        print(f"run.py: error: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())

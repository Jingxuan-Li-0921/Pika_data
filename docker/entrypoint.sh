#!/usr/bin/env bash

set -Eeuo pipefail

readonly ros_distro="${ROS_DISTRO:-humble}"
readonly ros_setup="/opt/ros/${ros_distro}/setup.bash"
readonly vendor_prefix="${PIKA_VENDOR_PREFIX:-/opt/pika/vendor/install}"
readonly workspace="${PIKA_WS:-/workspace/Pika_data/pika_ros}"
readonly overlay_prefix="${PIKA_OVERLAY_PREFIX:-${workspace}/install}"
readonly pyagxarm_root="${PIKA_PYAGXARM_ROOT:-/workspace/Pika_data/pyAgxArm}"
readonly device_environment="${PIKA_DEVICE_ENV:-/root/.config/pika/device.env}"

source_required() {
    local setup_file="$1"
    if [[ ! -f "${setup_file}" ]]; then
        printf '[pika-entrypoint] missing required setup: %s\n' "${setup_file}" >&2
        exit 1
    fi
    # ROS and colcon setup hooks use a few intentionally unset variables.
    # Keep nounset enabled for this wrapper, but disable it while sourcing
    # third-party environment hooks.
    set +u
    # shellcheck disable=SC1090
    source "${setup_file}"
    set -u
}

source_optional() {
    local setup_file="$1"
    if [[ -f "${setup_file}" ]]; then
        set +u
        # shellcheck disable=SC1090
        source "${setup_file}"
        set -u
    fi
}

prepend_path() {
    local variable_name="$1"
    local value="$2"
    local current_value="${!variable_name:-}"
    if [[ -z "${current_value}" ]]; then
        printf -v "${variable_name}" '%s' "${value}"
    else
        printf -v "${variable_name}" '%s:%s' "${value}" "${current_value}"
    fi
    # shellcheck disable=SC2163
    export "${variable_name}"
}

source_required "${ros_setup}"
source_required "${vendor_prefix}/setup.bash"

# `local_setup.bash` adds only the local overlay. This preserves the explicit
# order ROS base -> vendor underlay -> host-source overlay.
source_optional "${overlay_prefix}/local_setup.bash"
source_optional "${device_environment}"

# The SDK source is bind-mounted, so Python imports follow host edits without
# reinstalling pyAgxArm into the image.
if [[ -d "${pyagxarm_root}/pyAgxArm" ]]; then
    prepend_path PYTHONPATH "${pyagxarm_root}"
fi

# The vendor archive contains two compatible libsurvive locations and its
# generated hooks are normalized during image build. Keep both locations
# explicit for binaries launched without a colcon-generated environment.
prepend_path PATH "${vendor_prefix}/pika_locator/lib/pika_locator"
prepend_path PATH "${vendor_prefix}/pika_locator/lib"
prepend_path PATH "${vendor_prefix}/libsurvive/bin"
prepend_path LD_LIBRARY_PATH "/usr/local/lib"
prepend_path LD_LIBRARY_PATH "${vendor_prefix}/libsurvive/lib"
prepend_path LD_LIBRARY_PATH "${vendor_prefix}/pika_locator/lib"
prepend_path LD_LIBRARY_PATH "${vendor_prefix}/pika_locator/lib/plugins"

export PIKA_VENDOR_PREFIX="${vendor_prefix}"
export PIKA_WS="${workspace}"
export LC_NUMERIC="${LC_NUMERIC:-en_US.UTF-8}"

if (($# == 0)); then
    set -- bash
fi

exec "$@"

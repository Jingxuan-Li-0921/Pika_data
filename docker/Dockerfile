# syntax=docker/dockerfile:1.7

FROM ros:humble-ros-base-jammy

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

ARG ROS_DISTRO=humble
ARG PIKA_INSTALL_SHA256=522cc1d8721586cb9a8ff02129bf887718eb6f4b700f20e1ffe61a528ce2899d
ARG LIBREALSENSE_SHA256=c5d8bcbeccd897bd0b4f2b060dfea2af4d6ba6097e79c7b6760b11139a14f4d2

ENV DEBIAN_FRONTEND=noninteractive \
    LANG=en_US.UTF-8 \
    LANGUAGE=en_US:en \
    LC_ALL=en_US.UTF-8 \
    LC_NUMERIC=en_US.UTF-8 \
    ROS_DISTRO=${ROS_DISTRO} \
    ROS_VERSION=2 \
    ROS_PYTHON_VERSION=3 \
    PIKA_VENDOR_PREFIX=/opt/pika/vendor/install \
    PIKA_WS=/workspace/Pika_data/pika_ros \
    PYTHONUNBUFFERED=1 \
    PYTHONNOUSERSITE=1

# This is a development/runtime image: the packages below cover the local
# overlay, MoveIt, data tools, USB/Vive runtime, and the build of the bundled
# librealsense SDK. No host ROS, CUDA, Docker daemon, CAN, or udev changes are
# performed by this image.
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        ca-certificates \
        cmake \
        curl \
        file \
        freeglut3-dev \
        git \
        libboost-all-dev \
        libeigen3-dev \
        libgl1-mesa-dev \
        libglu1-mesa-dev \
        libglfw3-dev \
        libgtk-3-dev \
        libjsoncpp-dev \
        libopenvr-dev \
        libpcap-dev \
        libpcl-dev \
        libssl-dev \
        libudev-dev \
        libusb-1.0-0-dev \
        libx11-dev \
        locales \
        patchelf \
        pkg-config \
        python3-can \
        python3-colcon-common-extensions \
        python3-dev \
        python3-h5py \
        python3-matplotlib \
        python3-numpy \
        python3-opencv \
        python3-pandas \
        python3-pcl \
        python3-pip \
        python3-pytest \
        python3-requests \
        python3-scipy \
        python3-serial \
        python3-tqdm \
        python3-typing-extensions \
        python3-venv \
        python3-vcstool \
        python3-yaml \
        ros-${ROS_DISTRO}-controller-manager \
        ros-${ROS_DISTRO}-cv-bridge \
        ros-${ROS_DISTRO}-diagnostic-updater \
        ros-${ROS_DISTRO}-image-transport \
        ros-${ROS_DISTRO}-joint-state-publisher \
        ros-${ROS_DISTRO}-joint-state-publisher-gui \
        ros-${ROS_DISTRO}-moveit \
        ros-${ROS_DISTRO}-pcl-conversions \
        ros-${ROS_DISTRO}-pcl-msgs \
        ros-${ROS_DISTRO}-ros2-control \
        ros-${ROS_DISTRO}-ros2-controllers \
        ros-${ROS_DISTRO}-rosbag2-storage-mcap \
        ros-${ROS_DISTRO}-robot-state-publisher \
        ros-${ROS_DISTRO}-rviz2 \
        ros-${ROS_DISTRO}-tf2-eigen \
        ros-${ROS_DISTRO}-tf2-geometry-msgs \
        ros-${ROS_DISTRO}-tf2-sensor-msgs \
        ros-${ROS_DISTRO}-topic-tools \
        ros-${ROS_DISTRO}-xacro \
        unzip \
        zlib1g-dev \
    && locale-gen en_US.UTF-8 \
    && rm -rf /var/lib/apt/lists/*

# pyAgxArm is supplied through the host-source bind mount. Keep the SDK's
# Python dependency in the image rather than installing it on Ubuntu 20.04.
RUN python3 -m pip install --no-cache-dir \
        "python-can>=3.3.4" \
        "typing-extensions>=4.0.0"

WORKDIR /opt/pika

# Build the exact librealsense version shipped with this workspace. The
# graphical viewer and firmware download are deliberately disabled. The
# non-graphical tools remain enabled so realsense2_camera can run its
# rs-enumerate-devices configuration probe and provide diagnostics.
COPY pika_ros/source/librealsense-2.55.1.zip /tmp/librealsense-2.55.1.zip
RUN echo "${LIBREALSENSE_SHA256}  /tmp/librealsense-2.55.1.zip" | sha256sum -c - \
    && mkdir -p /opt/pika/src /opt/pika/build/librealsense \
    && unzip -q /tmp/librealsense-2.55.1.zip -d /opt/pika/src \
    && cmake -S /opt/pika/src/librealsense-2.55.1 \
        -B /opt/pika/build/librealsense \
        -DCMAKE_BUILD_TYPE=Release \
        -DCMAKE_INSTALL_PREFIX=/usr/local \
        -DCMAKE_INSTALL_LIBDIR=lib \
        -DBUILD_EXAMPLES=OFF \
        -DBUILD_GRAPHICAL_EXAMPLES=OFF \
        -DBUILD_PYTHON_BINDINGS=OFF \
        -DBUILD_TOOLS=ON \
        -DBUILD_UNIT_TESTS=OFF \
        -DBUILD_LEGACY_LIVE_TEST=OFF \
        -DBUILD_WITH_CUDA=OFF \
        -DBUILD_WITH_OPENMP=OFF \
        -DBUILD_GLSL_EXTENSIONS=OFF \
        -DBUILD_RS2_ALL=OFF \
        -DCHECK_FOR_UPDATES=OFF \
        -DIMPORT_DEPTH_CAM_FW=OFF \
        -DFORCE_RSUSB_BACKEND=ON \
    && cmake --build /opt/pika/build/librealsense --parallel "$(nproc)" \
    && cmake --install /opt/pika/build/librealsense \
    && ldconfig \
    && rm -rf /opt/pika/src /opt/pika/build /tmp/librealsense-2.55.1.zip

# Install the verified precompiled Pika payload as a vendor underlay. It is
# kept separate from the bind-mounted source overlay so local colcon builds
# can replace packages without destroying the locator binaries.
COPY pika_ros/source/install.zip /tmp/pika-install.zip
RUN echo "${PIKA_INSTALL_SHA256}  /tmp/pika-install.zip" | sha256sum -c - \
    && mkdir -p /opt/pika/vendor \
    && unzip -q /tmp/pika-install.zip -d /opt/pika/vendor \
    && test -f "${PIKA_VENDOR_PREFIX}/setup.bash" \
    && old_prefix='/home/ppn/git_repositories/pika_ros/install' \
    && old_libsurvive='/home/ppn/git_repositories/pika_ros/src/pika_locator/libsurvive' \
    && while IFS= read -r -d '' payload_file; do \
        if LC_ALL=C grep -Iq "${old_prefix}" "${payload_file}" \
            || LC_ALL=C grep -Iq "${old_libsurvive}" "${payload_file}" \
            || LC_ALL=C grep -Iq '/home/lin/miniconda3/envs/aloha/bin/python' "${payload_file}"; then \
          sed -i \
            -e "s|${old_prefix}|${PIKA_VENDOR_PREFIX}|g" \
            -e "s|${old_libsurvive}|${PIKA_VENDOR_PREFIX}/libsurvive|g" \
            -E -e 's|^#! ?/home/lin/miniconda3/envs/aloha/bin/python$|#!/usr/bin/env python3|' \
            "${payload_file}"; \
        fi; \
      done < <(find "${PIKA_VENDOR_PREFIX}" -type f -print0) \
    && vendor_rpath='$ORIGIN:$ORIGIN/../lib:$ORIGIN/../../lib:/opt/pika/vendor/install/lib:/opt/pika/vendor/install/libsurvive/lib:/opt/pika/vendor/install/pika_locator/lib:/opt/pika/vendor/install/pika_locator/lib/pika_locator:/opt/pika/vendor/install/pika_locator/lib/plugins:/usr/local/lib' \
    && while IFS= read -r -d '' payload_file; do \
        if file -b "${payload_file}" | grep -Eq 'ELF.*(executable|shared object)' \
            && readelf -d "${payload_file}" >/dev/null 2>&1; then \
          patchelf --set-rpath "${vendor_rpath}" "${payload_file}"; \
        fi; \
      done < <(find "${PIKA_VENDOR_PREFIX}" -type f -print0) \
    && rm -f /tmp/pika-install.zip \
    && ldconfig

COPY docker/entrypoint.sh /usr/local/bin/pika-entrypoint
RUN chmod 0755 /usr/local/bin/pika-entrypoint

WORKDIR /workspace/Pika_data
ENTRYPOINT ["/usr/local/bin/pika-entrypoint"]
CMD ["bash"]

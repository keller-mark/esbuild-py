#!/bin/bash

# Configure the libraries needed to build wheel packages on linux.
# This script is designed to be used by cibuildwheel as CIBW_BEFORE_ALL_LINUX

set -euo pipefail
set -x

source /etc/os-release

case "$ID" in
    alpine)
        apk update
        apk add wget
        BUILD_ARCH=$(uname -m)
        ;;
    debian)
        apt-get update
        apt-get -y upgrade
        apt-get -y install wget
        BUILD_ARCH=$(dpkg --print-architecture)
        ;;

    centos)
        yum install wget -y
        BUILD_ARCH=$(uname -m)
        ;;

    *)
        echo "$0: unexpected Linux distribution: '$ID'" >&2
        exit 1
        ;;
esac

echo $BUILD_ARCH

if [ "$BUILD_ARCH" = "x86_64" ]; then
    wget https://go.dev/dl/go1.20.12.linux-amd64.tar.gz
    tar -C /usr/local -xzf go1.20.12.linux-amd64.tar.gz
else
    wget https://go.dev/dl/go1.20.12.linux-386.tar.gz
    tar -C /usr/local -xzf go1.20.12.linux-386.tar.gz
fi

# TODO: switch go installers depending on architecture
export PATH=$PATH:/usr/local/go/bin
go get github.com/keller-mark/esbuild-py
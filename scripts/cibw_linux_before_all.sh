#!/bin/bash

# Configure the libraries needed to build wheel packages on linux.
# This script is designed to be used by cibuildwheel as CIBW_BEFORE_ALL_LINUX

set -euo pipefail
set -x

case "$ID" in
    debian)
        apt-get update
        apt-get -y upgrade
        apt-get -y install wget
        ;;

    centos)
        yum install wget -y
        ;;

    *)
        echo "$0: unexpected Linux distribution: '$ID'" >&2
        exit 1
        ;;
esac

wget https://go.dev/dl/go1.20.12.linux-amd64.tar.gz
tar -C /usr/local -xzf go1.20.12.linux-amd64.tar.gz
export PATH=$PATH:/usr/local/go/bin
go get github.com/keller-mark/esbuild-py
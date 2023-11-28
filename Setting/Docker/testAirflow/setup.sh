#!/bin/bash

set -e

if id "default" &>/dev/null; then
    echo "User 'default' already exists"
else
    useradd -m default
    echo "default ALL=(ALL:ALL) NOPASSWD: ALL" > /etc/sudoers.d/default
    chmod 0440 /etc/sudoers.d/default
fi

# 필요한 패키지 설치



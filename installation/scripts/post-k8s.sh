#!/bin/bash
mkdir -p $HOME/.kube 
sudo cp -i /etc/kubernetes/admin.conf  $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config

# Install Cilium 
CILIUM_CLI_VERSION=v0.12.11
CLI_ARCH=amd64
curl -L --fail --remote-name-all https://github.com/cilium/cilium-cli/releases/download/${CILIUM_CLI_VERSION}/cilium-linux-${CLI_ARCH}.tar.gz{,.sha256sum}  > /dev/null 2>&1
sha256sum --check cilium-linux-${CLI_ARCH}.tar.gz.sha256sum  > /dev/null 2>&1
sudo tar xzvfC cilium-linux-${CLI_ARCH}.tar.gz /usr/local/bin  > /dev/null 2>&1
rm cilium-linux-${CLI_ARCH}.tar.gz{,.sha256sum}  > /dev/null 2>&1

cilium install > /dev/null 2>&1

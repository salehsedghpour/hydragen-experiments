#!/bin/bash
# Download Istio version 1.14.0
curl -L https://istio.io/downloadIstio | ISTIO_VERSION=1.14.0 TARGET_ARCH=x86_64 sh - > /dev/null 2>&1

# Install Istio with a custom operator
 ~/istio-1.14.0/bin/istioctl install -y -f ~/scripts/configs/istio-operator.yaml > /dev/null 2>&1
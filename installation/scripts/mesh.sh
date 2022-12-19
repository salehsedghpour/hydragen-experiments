#!/bin/bash
curl -L https://istio.io/downloadIstio | ISTIO_VERSION=1.14.0 TARGET_ARCH=x86_64 sh - > /dev/null 2>&1

~/istio-1.14.0/bin/istioctl install --set profile=default -y > /dev/null 2>&1
#!/bin/bash

# Disable swap
sudo swapoff -a > /dev/null 2>&1
sudo sed -i '/ swap / s/^/#/' /etc/fstab > /dev/null 2>&1

# # install packages to allow apt to use a repository over HTTPS
# sudo apt-get install -y apt-transport-https

# Download the Google Cloud public signing key
sudo curl -fsSLo /etc/apt/keyrings/kubernetes-archive-keyring.gpg https://packages.cloud.google.com/apt/doc/apt-key.gpg > /dev/null 2>&1

# Add the Kubernetes apt repository
echo "deb [signed-by=/etc/apt/keyrings/kubernetes-archive-keyring.gpg] https://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee /etc/apt/sources.list.d/kubernetes.list > /dev/null 2>&1

# Update apt package index, install kubelet, kubeadm and kubectl, and pin their version:
sudo apt-get update -y > /dev/null 2>&1
sudo apt-get install -y kubelet=1.23.7-00 kubectl=1.23.7-00 kubeadm=1.23.7-00 > /dev/null 2>&1
sudo apt-mark hold kubelet kubeadm kubectl > /dev/null 2>&1 



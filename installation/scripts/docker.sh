#!/bin/bash

# upgrade 
sudo apt-get update -y > /dev/null 2>&1
sudo apt-get upgrade -y > /dev/null 2>&1

# install packages to allow apt to use a repository over HTTPS
sudo apt-get install -y  ca-certificates curl gnupg lsb-release  > /dev/null 2>&1

# Add Docker’s official GPG key:
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg > /dev/null 2>&1

# Use the following command to set up the repository:
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Update the apt package index:
sudo apt-get update > /dev/null 2>&1


# Install Docker engine 5:20.10.16~3-0~ubuntu-focal
VERSION_STRING=5:20.10.16~3-0~ubuntu-focal
sudo apt-get install -y docker-ce=$VERSION_STRING docker-ce-cli=$VERSION_STRING containerd.io docker-compose-plugin > /dev/null 2>&1

# Make Docker to start with systemd cgroup driver
sudo bash -c "cat > /etc/docker/daemon.json" <<EOF
{
  "exec-opts": ["native.cgroupdriver=systemd"]
}
EOF

sudo systemctl restart docker > /dev/null 2>&1






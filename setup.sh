#!/bin/bash

echo "This script updates and installs some necessary softwares. At the end, it will report its IP address for SSH"

# Change apt-get source to TUNA
sudo rm /etc/apt/sources.list
echo "deb http://mirrors.tuna.tsinghua.edu.cn/raspbian/raspbian/ stretch main non-free contrib" >> /etc/apt/sources.list
echo "deb-src http://mirrors.tuna.tsinghua.edu.cn/raspbian/raspbian/ stretch main non-free contrib" >> /etc/apt/sources.list
sudo rm /etc/apt/sources.list.d/raspi.list
echo "deb http://mirrors.tuna.tsinghua.edu.cn/raspberrypi/ stretch main" >> /etc/apt/sources.list.d/raspi.list

# Remove LibreOffice
sudo apt-get -y remove --purge libreoffice*
sudo apt-get -y clean
sudo apt-get -y autoremove

# Update softwares
sudo apt-get -y update
sudo apt-get -y upgrade

# Install some softwares
sudo apt-get -y install apache2 python python3 git-all nmap python-pip

# Enable SSH and VNC
sudo systemctl enable ssh
sudo systemctl enable vncserver-x11-serviced

echo "Your IP address is: "
ThisIP=`hostname -I`
echo $ThisIP
echo "Testing connection via nmap..." 
echo `nmap -sP $ThisIP`

git clone https://github.com/longyuxi/2019-genas-china-smart-device
cd 2019-genas-china-smart-device

## Under directory `2019-genas-china-smart-device`
sudo pip install -r requirements.txt

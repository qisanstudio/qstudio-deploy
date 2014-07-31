#! /usr/bin/env bash

# 完善语言配置
echo 'LANGUAGE="en_US:en"' | sudo tee --append /etc/default/locale > /dev/null
locale-gen --purge
sudo locale-gen en_US.UTF-8
sudo dpkg-reconfigure locales
echo "" >> ~/.bashrc
echo "export LC_ALL=en_US.UTF-8" >> ~/.bashrc
echo "" >> ~/.bashrc


# 基本库安装
sudo aptitude update
sudo aptitude -y upgrade
sudo aptitude install -y gcc
sudo aptitude install -y g++
sudo aptitude install -y git
sudo aptitude install -y libjansson-dev
sudo aptitude install -y python2.7
sudo aptitude install -y python2.7-dev
sudo aptitude install -y ruby
sudo aptitude install -y libpcre3
sudo aptitude install -y libpcre3-dev
sudo aptitude install -y python-pip
sudo aptitude install -y build-essential
sudo aptitude install -y postgresql


sudo pg_createcluster 9.3 main --start
sudo service postgresql restart   # 重启DB

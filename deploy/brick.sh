#! /usr/bin/env bash

# 完善语言配置
BASHRC = "$HOME/.bashrc"
echo "" >> $BASHRC
echo "export LC_ALL=en_US.UTF-8" >> $BASHRC
echo "" >> $BASHRC
source $BASHRC
echo 'LANGUAGE="en_US:en"' | sudo tee --append /etc/default/locale > /dev/null
locale-gen --purge
sudo locale-gen en_US.UTF-8
sudo dpkg-reconfigure locales



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
sudo aptitude install -y nginx
sudo aptitude install -y postgresql


sudo pg_createcluster 9.3 main --start
sudo service postgresql restart   # 重启DB

# 
sudo gem install sass

# 安装virtualenv环境
sudo apt-get install python-virtualenv
sudo pip install virtualenvwrapper
sudo pip install pep8
sudo pip install pyflakes
sudo pip install flake8

echo "export WORKON_HOME=$HOME/.virtualenvs" >> $BASHRC
echo "source /usr/local/bin/virtualenvwrapper.sh" >> $BASHRC

# 新建prod环境
mkvirtualenv "prod"
cd ~/qisanstudio
setvirtualenvproject

# 把node环境加入到virtualenv
pip install nodeenv
nodeenv --python-virtualenv

# 安装yeoman
npm cache clean
npm install -g yo
npm install -g generator-webapp

# 安装qisanstudio基础库
pip install -e 'git://github.com/qisanstudio/qstudio-launch.git#egg=qstudio-launch'
# 完成 launch 命令补齐调用
LAUNCH_COMPLETE="complete -C 'python -m studio.launch.complete' launch"
echo $LAUNCH_COMPLETE >> $VIRTUAL_ENV/bin/postactivate
#pip install -e 'git://github.com/qisanstudio/qstudio-core.git#egg=qstudio-core'


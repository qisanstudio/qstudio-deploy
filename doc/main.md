```Shell
#! /usr/bin/env bash


# edit timezone
sudo vim /etc/timezone
sudo dpkg-reconfigure tzdata

### sudo apt-get install libpq-dev         for psycopg2 install
### sudo apt-get install python2.7-dev     for uwsgi install

### http://pythonhosted.org//setuptools/setuptools.html?highlight=namespace#namespace-packages

# install virtualenv
sudo apt-get install python-virtualenv
pip install virtualenvwrapper
echo "export WORKON_HOME=/home/qisan/.virtualenvs" >> ~/.bashrc
echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc

# build env
mkvirtualenv $1


# for pip install uwsgi
sudo apt-get install libjansson-dev  # for uwsgi json
export UWSGI_PROFILE=gevent pip install uwsgi

# for node
pip install nodeenv
nodeenv --python-virtualenv          #把node环境加入到virtualenv
```

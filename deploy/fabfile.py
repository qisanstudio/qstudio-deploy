# -*- coding: utf-8 -*-

import os
import fabtools
from fabtools import require, python_setuptools
from fabric.api import env, local, run, sudo
from fabric.context_managers import prefix



env.hosts = ['microsite']
env.user = 'qstudio'
env.key_filename = '~/.ssh/id_rsa_droplet'
env.warn_only = True

PUB_KEY = os.path.join(os.path.abspath('.'), 'keys/id_rsa_droplet.pub')


def init_user(name):
    """
        create user
    """
    if not fabtools.user.exists(name):
        fabtools.user.create(name, password='studio',
                             shell='/bin/bash',
                             ssh_public_keys=PUB_KEY)
        require.users.sudoer(name)


def init_os():
    with prefix("sudo aptitude update"):
        sudo("aptitude -y upgrade")
        sudo("aptitude install -y gcc")
        sudo("aptitude install -y g++")
        sudo("aptitude install -y git")
        sudo("aptitude install -y libjansson-dev")
        sudo("aptitude install -y python2.7")
        sudo("aptitude install -y python2.7-dev")
        sudo("aptitude install -y ruby")
        sudo("aptitude install -y libpcre3")
        sudo("aptitude install -y libpcre3-dev")


def init_pyenv():
    '''
        init python envirment
    '''
    sudo("aptitude install -y python-pip")
    sudo("aptitude install -y build-essential")
    if not python_setuptools.is_setuptools_installed():
        python_setuptools.install_setuptools()
    python_setuptools.install('virtualenv', use_sudo=True)
    print '================================'
    python_setuptools.install([
        'virtualenvwrapper',
        'pep8',
        'pyfakes',
        'flake8'
    ], use_sudo=True)



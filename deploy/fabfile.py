# -*- coding: utf-8 -*-

import os
import fabtools
from fabtools import require, python_setuptools
from fabric.api import env


env.hosts = ['iefschina']
env.user = 'qisan'
env.key_filename = '~/.ssh/id_rsa_iefschina'

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


def install_server():
    '''
        install server
    '''
    require.deb.packages([
        'gcc',
        'g++',
        'git',
        'libjansson-dev',
        'python2.7',
        'python2.7-dev',
        'python-pip',
        'build-essential',
        'ruby',
        'libpcre3',
        'libpcre3-dev',
        'postgresql-9.3'
    ])


def init_pyenv():
    '''
        init python envirment
    '''
    python_setuptools.install([
        'vritualenv',
        'virtualenvwrapper',
        'pep8',
        'pyfakes',
        'flake8',
    ], use_sudo=True)

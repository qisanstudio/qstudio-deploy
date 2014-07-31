# -*- coding: utf-8 -*-

import os
import fabtools
from fabtools import require, python_setuptools
from fabric.api import env, local, run, sudo
from fabric.context_managers import prefix



env.hosts = ['microsite']
env.user = 'qstudio'#'root'
env.key_filename = '~/.ssh/id_rsa_droplet'
env.warn_only = True

PUB_KEY = os.path.join(os.path.abspath('.'), 'keys/id_rsa_droplet.pub')


MANAGER = {'name': 'qstudio', 'pwssword': 'studio'}

def create_user(name=MANAGER['name'], is_sudoer=True):
    """
        create user
    """
    if not fabtools.user.exists(name):
        fabtools.user.create(name, password=MANAGER['password'],
                             shell='/bin/bash',
                             ssh_public_keys=PUB_KEY)
        if is_sudoer:
            require.users.sudoer(name)


from fabric.operations import prompt
from fabric.utils import abort
from fabtools.files import is_dir
from fabtools.user import home_directory
from fabric.api import cd, put

def throw_brick(name=MANAGER['name'], workspace='qisanstudio'):
    if not fabtools.user.exists(name):
        r = prompt("%s does not exist, create it?(y/n)", default="yes")
        if r in ('y', 'Y', 'yes', 'YES'):
            create_user(name=name)
        else:
            abort("no user no brick!")

    home = home_directory(name)
    workspace_path = os.path.join(home, workspace)
    if not is_dir(workspace_path):
        run("mkdir -p %s" % workspace_path)
    put('brick.sh', workspace_path, mode=0755)


def test():
    put()


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
    python_setuptools.install([
        'virtualenv',
        'virtualenvwrapper',
        'pep8',
        'pyflakes',
        'flake8'
    ], use_sudo=True)



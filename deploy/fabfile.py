# -*- coding: utf-8 -*-

import os
from fabric.api import env, run, put
from fabric.operations import prompt
from fabric.utils import abort
import fabtools
from fabtools import require
from fabtools.files import is_dir
from fabtools.user import home_directory


__all__ = ['create_user', 'throw_brick']


MANAGER = {'name': 'qstudio', 'password': 'studio'}
SSH_D = os.path.join(os.path.abspath('.'), 'ssh.d')

print SSH_D


def _k(fn):
    return os.path.join(SSH_D, fn)

env.hosts = ['suibe']#['microsite']
env.user = 'qstudio'#'root'
env.key_filename = _k('droplet_rsa.priv')
env.warn_only = True


def create_user(name=MANAGER['name'], is_sudoer=True):
    """
        新建用户
        params:
            name => MANAGER['name'](default)
            is_sudoer => True(default)
    """
    if not fabtools.user.exists(name):
        fabtools.user.create(name, password=MANAGER['password'],
                             shell='/bin/bash',
                             ssh_public_keys=_k('id_rsa_droplet.pub'))
        if is_sudoer:
            require.users.sudoer(name)


def throw_brick(name=MANAGER['name'],
                workspace='qisanstudio',
                with_github=True):
    """
        向新环境传输一个brick脚本，初始化用。抛砖引玉！
        params:
            name => MANAGER['name'](default)
            workspace => 'qisanstudio'
            with_github => True(default)
    """
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
    if with_github:
        _github(name=name)


def _github(name=MANAGER['name']):
    ssh_path = '~/.ssh'
    if not is_dir(ssh_path):
        run("mkdir -p %s" % ssh_path)
    put(_k('qisanstudio_rsa.priv'), '~/.ssh', mode=0600)
    put(_k('config'), '~/.ssh', mode=0664)

# -*- coding: utf-8 -*-

import fabtools
from fabtools.require import users
from fabric.contrib.console import confirm
from fabric.api import env



env.hosts = ['iefschina']
env.user = 'qisan'
env.key_filename = '~/.ssh/id_rsa_iefschina'

# create user
def create_user(username):
    if not fabtools.user.exists(username):
        fabtools.user.create(username)


def modify_user(username, password):
    if fabtools.user.exists(username):
        fabtools.user.modify(username, password=password)


def add_pub_key(username):
    fabtools.user.add_ssh_public_key(username, '/Users/liuzhiyong/.ssh/github_rsa.pub')


def add_sudo(username):
    users.sudoer(username)


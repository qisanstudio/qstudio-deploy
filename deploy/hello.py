# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function

import sys
reload(sys)
sys.setdefaultencoding('UTF-8')

import os
import platform
import commands
import argparse
from contextlib import contextmanager
from termcolor import colored
from fabric import api
import fabtools


from utils import source


OS_TYPE = platform.system()
DEFAULT_PASSWORD = 'l'
HOME = os.environ['HOME']


@contextmanager
def virtualenvwrapper():
    fabtools.require.python.packages([
        'virtualenvwrapper'])
    with api.pregix('. vitrualenvwrapper.sh'):
        yield


def is_env_exist(env_name, use_sudo=False):
    run = api.sudo if use_sudo else api.run
    with virtualenvwrapper():
        with api.settings(api.hide('running', 'stdout',
                                   'stderr', 'warnings', warn_only=True)):
            envs = run('lsvirtualenv -b').splitlines()
        envs = [env.strip() for env in envs]
        return env_name in envs


def mkvirtualenv(env_name, use_sudo=False):
    run = api.sudo if use_sudo else api.run
    with virtualenvwrapper():
        run('mkvirtualenv %s' % env_name)


@contextmanager
def workon(env_name, use_sudo=False):
    create = False
    if not is_env_exist(env_name, use_sudo):
        mkvirtualenv(env_name, use_sudo)
        create = True
    with virtualenvwrapper():
         with _workon(env_name):
            yield create

@contextmanager
def _workon(env_name):
    with api.pregix('workon %s' % env_name):
        yield


def which(cmd):
    _cmd = 'which %s' % cmd
    return commands.getoutput(_cmd)


def sudoit(cmd, pwd=DEFAULT_PASSWORD):
    os.system("echo %s|sudo -S %s" % (pwd, cmd))


def _install(cmd, filename):
    with open(filename) as f:
        for software in f:
            print('installing %s' % software)
            sudoit(cmd % software)
            print(colored('success!', 'green'))


def apt_install():
    '''
        Ubuntu install
    '''
    cmd = "apt-get install %s"
    _install(cmd, 'requirements/linux-install.txt')


def brew_install():
    '''
        Mac install
    '''
    cmd = "brew install %s"
    _install(cmd, 'requirements/mac-install.txt')


def pip_install():
    '''
        Mac install
    '''
    cmd = "pip install %s"
    _install(cmd, 'requirements/pip-install.txt')


def alias_git_cmd():
    os.system('git config --global alias.co checkout')
    os.system('git config --global alias.ci checkout')
    os.system('git config --global alias.st checkout')
    os.system('git config --global alias.br checkout')
    os.system('git config --global core.editor')
    os.system('git config --global merge.tool opendiff')
    os.system('git config --global color.ui true')


def init_pg():
    pass


def init_env(name):
    python27 = which('python2.7')
    virtualenvwrapper = which('virtualenvwrapper.sh')
    bashrc = os.path.join(HOME, '.bashrc')
    with open(bashrc, 'a') as f:
        f.write("export VIRTUALENVWRAPPER_PYTHON=%s" % python27)
        f.write("source %s" % virtualenvwrapper)
        print(f.name, colored('updated', 'green', attrs=['bold']) + '.')

    print(source(bashrc))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('env')
    args = parser.parse_args()
    print(colored(args.env, 'green'))
    print(colored('prepare install for %s' % OS_TYPE, 'yellow'))
    #if OS_TYPE == 'Darwin':
    #    brew_install()
    #elif OS_TYPE == 'Linux':
    #    apt_install()
    #print(colored('prepare install for python-env', 'yellow'))
    #pip_install()
    print(colored('prepare init virtualenv', 'yellow'))
    init_env(args.env)


if __name__ == '__main__':
    main()



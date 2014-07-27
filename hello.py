# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function

import os
import sys
import platform
import argparse
from termcolor import colored

OS_TYPE = platform.system()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('env')
    args = parser.parse_args()
    print(colored(args.env, 'green'))
    print(colored(OS_TYPE, 'yellow'))


if __name__ == '__main__':
    main()

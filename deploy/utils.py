# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function

import os
from subprocess import Popen, PIPE


def source(script, update=True, clean=True):
    """
    Source variables from a shell script
    import them in the environment (if update==True)
    and report only the script variables (if clean==True)
    """

    global environ
    if clean:
        environ_back = dict(os.environ)
        os.environ.clear()

    pipe = Popen(". %s; env" % script, stdout=PIPE, shell=True)
    data = pipe.communicate()[0]

    env = dict((line.split("=", 1) for line in data.splitlines()))

    if clean:
        # remove unwanted minimal vars
        env.pop('LINES', None)
        env.pop('COLUMNS', None)
        environ = dict(environ_back)

    if update:
        environ.update(env)

    return env

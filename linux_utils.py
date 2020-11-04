# -*- coding: utf-8 -*-

import os
from subprocess import PIPE, run


def proc_by_name(name: str) -> MutableSequence:
    pattern = f"ps x  | egrep {name} | egrep -v 'grep | egrep'"

    pid_list = [int(pid.split()[0]) for pid in run(p, shell=True, stdout=PIPE, stderr=PIPE).stdout.decode().split('\n') if pid]

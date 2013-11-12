#!/usr/bin/env python
# coding: utf-8


"""
子进程结束会向父进程发送 SIGCHLD 信号
"""

import os
import signal
from time import sleep


def onsigchld(a, b):
    print '收到子进程结束信号'

signal.signal(signal.SIGCHLD, onsigchld)

pid = os.fork()

if pid == 0:
    print '我是子进程， pid是', os.getpid()
    os.sleep(2)
else:
    print '我是父进程， pid是', os.getpid()
    os.wait() #等待子进程结束

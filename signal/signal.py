#!/usr/bin/env python
# coding: utf-8

"""
接受信号的程序, 测试 多线程向这个进程发送信号， 会遗漏一些信号
"""
import os
import signal
from time import sleep
import Queue
#初始化队列
QCOUNT = Queue.Queue()
def onsignchld(a, b):
    print '收到SIGUSR1信号'
    sleep(2)
    #向队列写入1
    QCOUNT.put(1)

def exithanddle(s, e):
    raise SystemExit('收到终止命令')
# 绑定信号处理函数
signal.signal(signal.SIGUSR1, onsignchld)
signal.signal(signal.SIGINT, exithanddle)

while 1:
    print '我的pid是 ', os.getpid()
    print '我现在队列中的元素个数是', QCOUNT.qsize()
    sleep(2)

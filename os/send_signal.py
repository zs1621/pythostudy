#!/usr/bin/env python
# coding: utf-8

'''
使用多线程向另外一个进程发送信号
'''
import threading
import os
import signal

def sendusr1():
    print '发送信号'
    os.kill(9361, signal.SIGUSR1)

WORKER = []

#开19个线程
for i in range(1, 20):
    threadinstance =  threading.Thread(target=sendusr1)
    WORKER.append(threadinstance)

for i in WORKER:
    i.start()

for i in WORKER:
    i.join()

print 'main finish'

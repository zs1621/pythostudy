#!/usr/bin/env python
# coding: utf-8

import signal
import time

def receive_alarm(signum, stack):
    print 'Alarm:', time.time()


signal.signal(signal.SIGALRM, receive_alarm)
signal.alarm(2)


print 'Before:', time.time()

time.sleep(10)

print 'After:', time.time()

"""
注意: Signal 只有主线程才能接受信号
"""

#!/usr/bin/python
# coding: utf-8

"""
用python 实现单例模式

所谓单例模式:保证一个类仅有一个实例， 并提供一个访问他的全局访问点
"""
import threading
import os

class IOLoop(object):

    _instance_lock = threading.Lock()

    @staticmethod
    def instance():
        if not hasattr(IOLoop, "_instance"):
            """
            这里理解with  threading.Lock()会在执行完下面的body后做个`threading.release()`
            """
            with IOLoop._instance_lock:
                if not hasattr(IOLoop, "_instance"):
                    IOLoop._instance = IOLoop()
                else:
                    print 'has exit'
        else:
            print 'has exit instance'
        return IOLoop._instance

    @staticmethod
    def initialized():
        return hasattr(IOLoop, "_instance")

print IOLoop.initialized()
#ioloop = IOLoop.instance()
ioloop = IOLoop.instance()
print IOLoop.initialized()
ioloop1 = IOLoop.instance()
print IOLoop.initialized()

#!/usr/bin/env python
# coding: utf-8
"""
inspect.getargspec 介绍

return a tuple of four things (args, varags, keywords, defaults)

args:  a list of argument names
varags: * or None
kewords: **  or  None
defaults: a tuple of argument values or None if no default arguments

"""
import inspect
def a():
    print 'a'
print inspect.getargspec(a)  # ArgSpec(args=[], varargs=None, keywords=None, defaults=None)


def b(arg1, arg2):
    print 'b'
    print 'dd'
print inspect.getargspec(b)  # ArgSpec(args=['arg1', 'arg2'], varargs=None, keywords=None, defaults=None)


def c(arg1, *m, **n):
    print 'c'
print inspect.getargspec(c)  # ArgSpec(args=['arg1'], varargs='m', keywords='n', defaults=None)


def d(arg1, arg2=1, *m, **n):
    print 'd'
print inspect.getargspec(d)  # ArgSpec(args=['arg1', 'arg2'], varargs='m', keywords='n', defaults=(1,))


"""
Argspec  TBC
"""

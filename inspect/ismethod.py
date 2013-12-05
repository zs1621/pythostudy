#!/usr/bin/env python
# coding: utf-8

import inspect

class Test(object):
    def funtest(self):
        print 'pp'

print inspect.ismethod(Test.__dict__['funtest'])
print inspect.ismethod(Test.funtest)
print inspect.ismethod(Test().funtest)
print getattr(Test, 'funtest')
print getattr(Test(), 'funtest')

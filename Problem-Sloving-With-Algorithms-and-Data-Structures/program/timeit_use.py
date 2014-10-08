#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   Rhapsodyzs
#   E-mail  :   zs1213yh@gmail.com
#   Date    :   14/10/08 14:07:14
#   Desc    :  timeit use 
#
#import timeit
#popzero = timeit.Timer("x.pop(0)", "from __main__ import x")
#
#popend = timeit.Timer("x.pop()", "from __main__ import x")
#
#print ("pop(0)          ,     pop()")
#
#for i in range(1000000, 100000001, 1000000):
#    x = list(range(i))
#    pt = popend.timeit(number=1000)
#    x = list(range(i))
#    pz = popzero.timeit(number=1000)
#    print("%15.5f, %15.5f" %(pz, pt))
#

import timeit
t = timeit.Timer("print 'main statement'", "print 'setup'")
print ('Timeit:')
print t.timeit(4)

#!/usr/bin/env python
# coding:utf-8


import os, sys

"""
`os.pipe(): create a pipe. Return a pair of file
descriptors(r, w) usable for reading and writing, respectively`
"""

#创建管道
r, w = os.pipe()
#创建子进程
processid = os.fork()


if processid:
    #关闭管道写端
    os.close(w)
    #从读端读数据知道子进程死亡或者关闭
    r = os.fdopen(r)
    str = r.read()
    print 'text = ', str
    sys.exit(0)
else:
    #关闭管道写端
    os.close(r)

    w = os.fdopen(w, 'w')
    w.write("Text written by child...")
    w.close()
    print "Child closing"
    sys.exit(0)



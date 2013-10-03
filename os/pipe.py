#!/usr/bin/env python
# coding:utf-8


import os, sys

"""
`os.pipe(): create a pipe. Return a pair of file
descriptors(r, w) usable for reading and writing, respectively`
"""
r, w = os.pipe()
processid = os.fork()


if processid:
    os.close(w)
    r = os.fdopen(r)
    str = r.read()
    print 'text = ', str
    sys.exit(0)
else:
    os.close(r)
    w = os.fdopen(w, 'w')
    w.write("Text written by child...")
    w.close()
    print "Child closing"
    sys.exit(0)



#!/usr/bin/env python
# condig: utf-8

"""
the method `fdopen()` returns an open file object
connected to the file description `fd`. Then you can
perform all the defined functions on the file object.
"""

import os
#Open a file
fd = os.open('foo.txt', os.O_RDWR | os.O_CREAT)

# now get a file object for the above file.
fo = os.fdopen(fd, 'w+')
print "Current I/O pointer position :%d" % fo.tell()
# tell the current position
fo.write("Python is a great language.\nYeah its great!!\n")

#Now read the file from the beginning
os.lseek(fd, 0, 0)
str = os.read(fd, 100)
print "Read String is:", str

print "Current I/O pointer position :%d" % fo.tell()

fo.close()

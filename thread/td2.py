#!/usr/bin/env python
# coding: utf-8

import Queue
import threading
import urllib2

def get_url(q, url):
    q.put(urllib2.urlopen(url).read())

theurls = '''http://awish.at http://iworkout.cn'''.split()

q = Queue.Queue()

for u in theurls:
    t = threading.Thread(target=get_url, args = (q, u))
    t.daemon = True
    t.start()

s = q.get()
print s

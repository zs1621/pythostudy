#!/usr/bin/env python
# coding: utf-8

import socket
s = socket.socket()
s.connect(("localhost", 8888))
print s.recv(1024)
s.close

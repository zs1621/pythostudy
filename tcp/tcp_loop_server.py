#!/usr/bin/env python
# coding: utf-8


from tornado import ioloop
from tornado import iostream
import socket
import errno
import functools


def handle_connection(client, address):
    client.send("Hello world from A simple tcpserver")
    client.close

def connection_read(sock, fd, events):
    while True:
        try:
            connection, address = sock.accept()
        except socket.error, e:
            if e.args[0] not in (errno.EWOULDBLOCK, errno.EAGAIN):
                raise
            return
        connection.setblocking(0)
        handle_connection(connection, address)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.setblocking(0)
sock.bind(("localhost", 8888))
sock.listen(128)

print '----------------'
io_loop = ioloop.IOLoop.instance() #这里我们在 tornado -> util.py 里做了些log , 具体见下
print "============="
callback = functools.partial(connection_read, sock)
io_loop.add_handler(sock.fileno(), callback, io_loop.READ)
io_loop.start()

"""

```
    def __new__(cls, **kwargs):
        print (cls, 'cls')
        base = cls.configurable_base()
        args = {}
        if cls is base:
            print (cls)
            impl = cls.configured_class()
            print (impl, 'impl')
            if base.__impl_kwargs:
                args.update(base.__impl_kwargs)
        else:
            impl = cls
        args.update(kwargs)
        instance = super(Configurable, cls).__new__(impl)
        print (instance, 'instance')
        # initialize vs __init__ chosen for compatiblity with AsyncHTTPClient
        # singleton magic.  If we get rid of that we can switch to __init__
        # here too.
        instance.initialize(**args)
        return instance


```

最后的输出呢
```

----------------
                                                                            │<class 'tornado.ioloop.IOLoop'> cls
                                                                            │<class 'tornado.ioloop.IOLoop'>
                                                                            │<class 'tornado.platform.epoll.EPollIOLoop'> impl
                                                                            │<tornado.platform.epoll.EPollIOLoop object at 0x91f4f6c> instance
                                                                            │hello

 =============
```
"""

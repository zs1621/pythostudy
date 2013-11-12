#!/usr/bin/env python
# coding: utf-8

"""
参考 [with statement](http://effbot.org/zone/python-with-statement.htm)
[with china](http://jianpx.iteye.com/blog/505469)

下面理解`with`
"""

#1--------------------------1
#打开文件，从文件里面读取数据， 然后打印到终端， 之后关闭文件
# 方案1 用函数把公共的部分抽取出来
"""
这里 "set things up"可以打开文件， "tear things down"关闭文件，释放或者去除资源
使用 try .. finally 可以保证`tear things down`被执行
```
def controlled_execution(callback):
        set things up
        try:
                callback(thing)
        finally:
                tear things down

def my_function(thing):
        do something

contrlled_execution(my_function)
```

这种方式的缺点就是啰嗦，特别是你需要改变本地变量
"""

filename = 'ko.py'

def output(content):
    print content

def controlled_execution(func):
    #prepare thing
    f = None
    try:
        f = open(filename, 'r')
        content = '1' + f.read()
        if not callable(func):
            return
        func(content)
    except IOError, e:
        print 'Error %s' % str(e)

    finally:
        if f:
            #tear thing down
            f.close()

def test():
    controlled_execution(output)

test()


#2-----------------------------------------2
"""
第二种方案 使用迭代，然后 for -in 循环

```
def controlled_execution():
        set things up
        try:
                yield thing
        finally:
                tear things down

for thing in controled_execution():
        do something with thing
```
缺点： 明明之需要执行一次却要加个循环
"""
#yield solution

def controlled_execution():
    f = None
    try:
        f = open(filename, 'r')
        thing = f.read()
        yield thing
    except IOError, e:
        print 'Error %s' % str(e)
    finally:
        if f:
            f.close()

def test2():
    for content in controlled_execution():
        output(str(2) + content)
test2()

#3----------------------------3
"""
用类的方式加上 with 实现
```
class controlled_execution:
        def __enter__(self):
                set things up
                return thing
        def __exit__(self, type, value, traceback):
                tear things down
with controlled_execution() as thing:
        some code
```

`with`被执行， python 调用 `__enter__`方法,  然后把`__enter__`返回的值赋给`as`后面的变量, 然后执行 `body` ,不管`body`执行了什么， 都会调用守护对象的 `__exit__`方法
"""

class controlled_execution(object):
    def __init__(self, filename):
        self.filename = filename
        self.f = None

    def __enter__(self):
        try:
            f = open(self.filename, 'r')
            content = f.read()
            return content
        except IOError as e:
            print (e)
    def __exit__(self, type, value, traceback):
        if self.f:
            print ('type:%s, value: %s, traceback: %s' %(str(type), str(value), str(traceback)))
            self.f.close()

with controlled_execution(filename) as thing:
    if thing:
        print str(3) + thing

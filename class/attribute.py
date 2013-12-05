#!/usr/bin/env python
# coding: utf-8

"""
In Python, only class attributes can be defined here; data attributes are defined in the __init__ method.
"""
class Test:
    a = 0 #class attributes
    def __init__(self):
        self.a += 1 #data attributes

print(Test.a)
print(Test().a)



"""
如果想改变 类的属性
"""

class counter:
    count = 0
    def __init__(self):
        self.__class__.count += 1
        #self.count = 9

print counter, '---' # __main__.counter
print counter.count # 0
c = counter() # 这里创建类实例  会影响到类的自身属性值变化 
print c.count # 1
print counter.count # 1 

d = counter() # 第一次创建实例后， 类的count 属性值变为1  
print d.count # 2
print c.count # 2
print counter.count # 2 # 类的属性  是被类和类实例共享

"""
如果有兴趣可以看下将注释的self.count = 9 运行  能很明显的了解 类属性和实例属性的区别
"""

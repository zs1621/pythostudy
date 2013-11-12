#-*- coding:utf-8 -*-
# 函数修饰符：对原有函数做一层包装
# 来自 ‘http://www.cnblogs.com/xupeizhi/archive/2013/02/07/2908600.html’
# 在看下 'http://blog.csdn.net/thumb3344/article/details/5645124'

def de(f):
    def _call_():
        print '------------------------'
        return f()
    print '================='
    return _call_

@de
def func1():
    print 'i am function func1'

@de
def func2():
    print 'i am function func2'


if __name__ == '__main__':
    #func1()
    #func2()
    pass
#如果注释`func1()` `func2()`, 运行可以看到输出！说明`@de`会运行`de`函数!然后再去掉注释, 运行后 您呢个看到de()其作用了  de就是对func1, func2的共同操作

print '第一段结束'
# 注意1:
## 修饰符等价与包装调用:
'''
@de
def func1:
----等价与----
func1 = de(func1)
'''
# 注意2:
## 修饰函数必须返回一个"可调用对象"

def de(f):
    def _call_():
        return f()
    return _call_ #返回的是一个函数体， 而非调用_call_


import sys
import traceback

def de1(f):
    def _call_(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except:
            print 'param type error'
    return _call_

@de1
def func1(lst1, lst2):
    for item in lst1 + lst2:
        print item
@de1
def func2(dic):
    for k, v in dic.items():
        print k, v

if __name__ == '__main__':
    func1([1,2], [3,4])
    func2([5,6])

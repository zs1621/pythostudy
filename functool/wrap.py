#!/usr/bin/env python
# coding: utf-8

from functools import wraps, partial

def my_decorator(f):
    #@wraps(f)
    def wrapper(*args, **kwargs):
        print 'Calling decorated function'
        return f(*args, **kwargs)
    return wrapper

@my_decorator
def example():
    """Docstring"""
    print 'call example function'

example()
print example.__doc__
print example.__name__

"""
为了修正函数属性   加入 functools.wraps 修饰符即可解决
"""


"""
具体 functools.wraps 代码实现
"""

WRAPPER_ASSIGNMENTS = ('__module__', '__name__', '__doc__')
WRAPPER_UPDATES = ('__dict__',)

def update_wrapper(wrapper,
                wrapped,
                assigned = WRAPPER_ASSIGNMENTS,
                updated = WRAPPER_UPDATES):
    for attr in assigned:
        setattr(wrapper, attr, getattr(wrapped, attr))
    for attr in updated:
        getattr(wrapper, attr).update(getattr(wrapped, attr, {}))
    return wrapper

def wraps(wrapped,
                assigned = WRAPPER_ASSIGNMENTS,
                updated = WRAPPER_UPDATES):
    return partial(update_wrapper, wrapped = warpped,
                    assigned = assigned, updated = updated)

"""
这里需要注意 return partial 函数  其实就是  update_wrapper(wrapper, ...)

wrapper参数 就是 wrapper 函数
具体看如下代码

"""
def add(a, b):
    return a + b

add_two = partial(add, b=2)

print add_two(5)

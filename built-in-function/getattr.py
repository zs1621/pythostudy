#!/usr/bin/env python 
# coding: utf-8

"""
介绍 getattr 定义 返回任何对象的任何属性.
参考 [getattr](http://www.diveintopython.net/power_of_introspection/getattr.html)
"""

"""
**`getattr`与 python 内在数据类型**
"""
li = ["larry", "curly"]
li.pop # 得到 `list` 的 `pop` 方法 , 注意这不是调用此方法,指得是方法本身 
print li.pop # <built-in method pop of list object at 0xb72c61ac>

getattr(li, "pop") # 此函数也返回 `pop` 方法, 但是方法名是作为`getattr`一个字符参数, 从定义可知 `list` 是 `object` , `pop` 是 `attribute`


print getattr(li, "pop")() #此处是调用 所以打印出 `curly`

"""
**`getattr`与 模块**
"""
import time 

print time.time#<built-in function time>
print getattr(time, "time") #<built-in function time>

print type(getattr(time, "time")) #<type 'builtin_function_or_method'>
print type(time.time) # <type 'builtin_function_or_method'>

print callable(getattr(time, "time")) #既然是函数或方法 ， 那自然是可以调用的   True


# coding: utf-8
##这里解释下 cached_property decorator


#首先贴处 cached_property 源码

class _Missing(object):

    def __repr__(self):
        return 'no value'

    def __reduce__(self):
        return '_missing'

_missing = _Missing()

class cached_property(object):
    def __init__(self, func, name=None, doc=None):
        self.__name__ = name or func.__name__
        self.__module__ = func.__module__
        self.__doc__ = doc or func.__doc__
        self.func = func

    def __get__(self, obj, type=None):
        if obj is None:
            return self
        value = obj.__dict__.get(self.__name__, _missing)
        if value is _missing:
            value = self.func(obj)
            obj.__dict__[self.__name__] = value
        return value



class Foo(object):
	@cached_property
	def bar(self):
		return 'dddd'

foo = Foo()
bar = foo.bar
print bar 
# dddd 
"""
第一次取foo.bar, 调用bar方法，并设置方法的返回值给foo.bar.所以第二次就不会执行此方法: 第一次调用后方法就被替代了
"""


foo.bar = 'dd0000'


print foo.bar
	
# dd0000
"""
现在bar是一个简单的属性  可以任意赋值
"""


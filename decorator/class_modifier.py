#-*- coding:utf-8 -*-
# 来自 ‘http://blog.csdn.net/openxmpp/article/details/8779691’
print '无修饰符'
class MyClass():
    def thisIsClassMethod(self):
        print "this is a class method"
if __name__ == "__main__":
    c = MyClass()
    MyClass.thisIsClassMethod(c) #调用时传入参数c,否则编译错误

print 'classmethod 修饰符'
class MyClass1():
    @classmethod
    def thisIsClassMethod(cls, parameter):
        print "this is a class method"
        print cls.__name__
        print type(cls)
if __name__ == "__main__":
    MyClass1.thisIsClassMethod(None)


print 'property 修饰符'

class MyClass2():
    def __init__(self, num):
        self._Num = num

    @property
    def Num(self):
        return self._Num

if __name__ == "__main__":
    c = MyClass2(100)
    print c.Num #这里的访问形式看起来是访问一个属性，但其实是调用一个方法

print 'staticmethod 修饰符'
'''
被staticmethod修饰符的表示这是一个类的静态方法，可以被类直接调用， 与@classmethod 的区别在于 classmethod对应的方法的地一个参数为cls, 为类的类型， 而staticmethod 不是
'''

class MyClass3:
    @staticmethod
    def thisIsStaticMethod():
        print 'This is static method'

if __name__ == '__main__':
    MyClass3.thisIsStaticMethod()

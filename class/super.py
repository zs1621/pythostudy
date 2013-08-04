#!/usr/bin/env python
# coding:utf-8
# 注意 super(B, self).method()  这一步是执行B的父类的方法

#class D(object):
#    def foo(self):
#        print "class D"
#        
#class B(D):
#    pass
#    
#class C(D):    
#    def foo(self):
#        print "class C"
#        
#class A(B, C):
#    pass
#    
#f = A()
#f.foo()

#class A(object):
#  def __init__(self):
#   print "enter A"
#   super(A, self).__init__()  # new
#   print "leave A"
#
#class B(object):
#  def __init__(self):
#   print "enter B"
#   super(B, self).__init__()  # new
#   print "leave B"
#
#class C(A):
#  def __init__(self):
#   print "enter C"
#   super(C, self).__init__()
#   print "leave C"
#
#c = C()

#class A(object):
#  def __init__(self):
#   print "enter A"
#   super(A, self).__init__()  # new
#   print "leave A"
#
#class B(object):
#  def __init__(self):
#   print "enter B"
#   super(B, self).__init__()  # new
#   print "leave B"
#
#class C(A):
#  def __init__(self):
#   print "enter C"
#   super(C, self).__init__()
#   print "leave C"
#
#class D(A):
#  def __init__(self):
#   print "enter D"
#   super(D, self).__init__()
#   print "leave D"
#class E(B, C):
#  def __init__(self):
#   print "enter E"
#   super(E, self).__init__()  # change
#   print "leave E"
#
#class F(E, D):
#  def __init__(self):
#   print "enter F"
#   super(F, self).__init__()  # change
#   print "leave F"
#
#f = F()

class D(object):
    def foo(self):
        print "class D"
        
        
class B(object):
    def foo(self):
        print "class B"
        super(B,self).foo()
    
class C(D):    
    def foo(self):
        print "class C"
        super(C,self).foo()
        
class A(B,C):
    print "class A"
    pass
print 'MRO:',[x.__name__ for x in A.__mro__] 
    
f = A()
f.foo()

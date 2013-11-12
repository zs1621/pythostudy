#!/usr/bin/env python
# coding: utf-8

"""
__new__(): New instance creation

New-style classes have a new special method name, __new__(), this is called on instantiation before the construcotr. it handles the creation of a new instance

[new explation](http://infohost.nmt.edu/tcc/help/pubs/python/web/new-new-method.html)

"""


"""
the document define

Called to create a new instance of class cls.__new__() is a static method (special-cased so you need not declare it as such) that takes the class of which an instance was requested as its first argument. The remaining arguments are thos passed to the object constructor expression(the call to the class). the return value of __new__() should be the new object instance(usually an instance of cls)

[new document](http://docs.python.org/2/reference/datamodel.html)
"""


"""

Typical implementations create a new instance of the class by invoking the superclass's __new__() method using `super(currentclass, cls).__new__(cls[, ...])` with appropriate arguments and then modifying the newly-created instance as necessary before returning it.
"""

class A(object):
    def __init__(self):
        print ("in init")
    def __new__(self):
        print ("in new")

A()

#!/usr/bin/env python
# coding: utf-8

class MyAbstractClass():
    	def method1(self):
		raise NotImplementedError()


class MyClass(MyAbstractClass): 
	def method1(self):
		print 'ok'
	

MyAbstractClass().method1()

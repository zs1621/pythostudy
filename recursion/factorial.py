#!/usr/bin/env python
# coding: utf-8

"""
factorial function
"""

def factorial(num):
	if num < 0:
		raise TypeError 
	if num >= 0 and num <=1:
		return 1
	else:
		return factorial(num - 1) * num

#print factorial(-1)


"""
reverse a list
"""
def reverse(lister, a):
	if len(lister) == 0:
		return a
	else:
		last = lister.pop()
		a.append(last)
		return reverse(lister, a)

print reverse([3,4,5], [])

#! /usr/bin/env python
# coding: utf-8

"""

define a Stack use list

"""

class Stack(object):
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def push(self, item):
		self.items.insert(0,item)

	def pop(self):
		return self.items.pop(0)

	def peek(self):
		return self.items[len(self.items) - 1]

	def size(self):
		return len(self.items)
"""
define parChecker 

检测括号是否对等匹配  计算机语言中的括号都是一开一合的 下面的程序就是检测是否已知的括号是否对等

"""

def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top,symbol):
                       balanced = False
        index = index + 1
    if balanced and s.isEmpty():
        return True
    else:
        return False

def matches(open,close):
    opens = "([{"
    closers = ")]}"
    return opens.index(open) == closers.index(close)




print(parChecker('({[[}('))

#!/usr/bin/env python
# coding: utf-8


"""

无序列表: 链表

"""


"""
结点类  Node
"""

class Node(object):
	def __init__(self, initdata):
		self.data = initdata
		self.next = None

	def getData(self):
		return self.data

	def getNext(self):
		return self.next

	def setData(self, newdata):
		self.data = newdata

	def setNext(self, newnext):
		self.next = newnext


"""
无序列表 类   由Node构建
"""

class UnorderedList(object):
	def __init__(self):
		self.head = None
		self.tail = None

	def isEmpty(self):
		return self.head == None

	def add(self, item):
		temp = Node(item)
		temp.setNext(self.head)
		if self.head != None:
			self.head = temp
		else:
			self.head = temp
			self.tail = self.head
			
	def length(self):
		current = self.head
		count = 0
		while current != None:
			count = count + 1
			current = current.getNext()
			print current
		return count
	def search(self, item):
		current = self.head
		found = False
		while current != None and not found:
			if current.getData() == item:
				found = True
			else:
				current = current.getNext()
		return found

	"""
	先找到item ,把item前面的元素setNext() -> item item.getNext()
	"""
	def remove(self, item):
		current = self.head
		previous = None
		found = False
		while not found:
			if current.getData() == item:
				found = True
			else:
				previous = current
				current = current.getNext()
		if previous == None:
			self.head = current.getNext()
		else:
			previous.setNext(current.getNext())

	def append(self, item):
		#print self.tail.getData()
		#print self.head.getData()
		temp = Node(item)
		tail = self.tail
		tail.setNext(temp)
		self.tail = temp 

	def insert(self, loc, item):
		pass
		#self

a = UnorderedList()
a.add(3)
a.add(4)
#a.add(5)
a.append(8)
#a.append(9)
print a.length()
#print a.tail.getData()
#print a.head.getData()
			
			

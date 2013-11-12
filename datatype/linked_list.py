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
                if current.getData() == self.tail.getData() \
                                and current.getNext() == None:
                    self.tail = previous
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    """
     append time complexity is O(1)

    """
    def append(self, item):
        newNode = Node(item)
        if self.head is None:
            self.head = newNode
        else:
            self.tail.setNext(newNode)
        self.tail = newNode

    """
     遍历整个链表

    """
    def traverse(self):
        item = self.head
        while item:
            print item.getData(),'--'
            item = item.getNext()

    def insert(self, loc, item):
        length = self.length()
        if loc < length:
            current = self.head
            previous = None
            i = 0
            while i != loc:
                previous = current
                current = current.getNext()
                i = i + 1
            if i == loc:
                if previous != None:
                    tmp  = Node(item)
                    previous.setNext(tmp)
                    tmp.setNext(current)
                else:
                    self.add(item)

        elif loc == length:
            self.append(item)
        else:
            raise ('loc  %d exceed the range') %loc


a = UnorderedList()
a.add(3)
a.traverse()
a.append(8)
a.traverse()
a.append(9)
a.traverse()
a.insert(3,1)
a.traverse()
a.remove(1)
a.traverse()
print a.length()
#while k:
#       print k.getData()
#       k = k.getNext()
#print a.tail.getData()
#a.print_list()
#print a.tail.getData()
#print a.length()
#a.add(5)
#print a.length()
#a.insert(2, 7)

#a.length()
#a.add(5)
#a.remove(8)
#print a.length()
#print a.search(3)

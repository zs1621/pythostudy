# coding: utf-8

#注意这里的Person() 括弧里的object ,有这个object的话  没有@aa.setter 那么p.aa 会报错 , 但是在第二个例子中 即使没有定义set 也可以赋值
# 两者的区别就是前者是 new-style class ,后者是 old-style class 
# 这是因为在new-style class 中， 规定是这样的
class Person(object):
	def __init__(self):
		self.aaa = 6

	@property
	def aa(self):
		return self.aaa + 2

	@aa.setter
	def aa(self, new_value):
		self.aaa = new_value

if __name__ == '__main__':
	p = Person()
	print p.aa
	p.aa = 5
	print p.aa


class People:
	def __init__(self):
		self.aaa = 6
	
	@property
	def aa(self):
		return self.aaa
k = People()
print k.aa
k.aa = 9
print k.aa

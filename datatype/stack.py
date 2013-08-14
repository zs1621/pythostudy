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

"""
利用堆栈进行表达式转换  
infix -> Postfix 
"A + B * C" -> ABC*+
"""
def infixToPostfix(infixexpr):
		prec = {}
		prec["*"] = 3
		prec["/"] = 3
		prec["+"] = 2
		prec["-"] = 2
		prec["("] = 1
		opStack = Stack()
		postfixList = []
		tokenList = infixexpr.split()

		for token in tokenList:
			if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
				postfixList.append(token)
			#左括弧 推入栈 
			elif token == '(':
				opStack.push(token)
			#如果遇到右括弧  
			elif token == ')':
				topToken = opStack.pop()
				while topToken != '(':
					postfixList.append(topToken)
					topToken = opStack.pop()
			else:
				while (not opStack.isEmpty()) and \
						(prec[opStack.peek()] >= prec[token] ):
							postfixList.append(opStack.pop())
				opStack.push(token)
		while not  opStack.isEmpty():
			postfixList.append(opStack.pop())
		return "".join(postfixList)

print (infixToPostfix("A + C * D"))


"""
Posfix evlauation
计算  

"""
def postfixEval(postfixExpr):
	operandStack = Stack()
	tokenList = postfixExpr.split()

	for token in tokenList:
		if token in "0123456789":
			operandStack.push(int(token))
		else:
			operand2 = operandStack.pop()
			operand1 = operandStack.pop()
			result = doMath(token, operand1, operand2)
			operandStack.push(result)
	return operandStack.pop()
def doMath(op, op1, op2):
	if op == "*":
		return op1 * op2
	elif op == "/":
		return op1 / op2
	elif op == "+":
		return op1 + op2
	else:
		return op1 - op2



print(postfixEval("7 8 *"))

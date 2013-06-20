#!/usr/bin/env python
#-*-coding='utf-8'-*-

# Define LogicGate Class
# One argument n-> label 
class LogicGate:
	def __init__(self, n):
		self.label = n
		self.output = None

	def getLabel(self):
		return self.label

	def getOutput(self):
		self.output = self.performGateLogic()
		return self.output

class BinaryGate(LogicGate):
	def __init__(self, n):
		LogicGate.__init__(self, n)
		self.pinA = None
		self.pinB = None

	def getPinA(self):
		return int(input("Enter Pin A input for gate " + \
				self.getLabel() + "-->"))
	def getPinB(self):
		return int(input("Enter Pin B input for gate " + \
				self.getLabel() + "-->"))

class UnaryGate(LogicGate):
	def __init__(self, n):
		LogicGate.__init__(self, n)
		self.pin = None
	def getPin(self):
		return int(input("Enter Pin input for gate " + \
				self.getLabel() + "-->"))

# AndGate class
class AndGate(BinaryGate):
	def __init__(self, n):
		BinaryGate.__init__(self, n)
	def performGateLogic(self):
		a = self.getPinA()
		b = self.getPinB()
		if a == 1 and b == 1:
			return 1
		else:
			return 0

g1 = AndGate("G1")
print(g1.getOutput())

class Connector:
	def __init__(self, fgate, tgate):
		self.fromgate = fgate
		self.togate = tgate
		tgate.setNextPin(self)
	def getFrom(self):
		return self.fromgate
	def getTo(self):
		return self.togate 

	def setNextPin(self, source):
		if self.pinA = None:
			self.pinA = source
		else:
			if self.pinB = None:
				self.pinB = source
			else:
				raise RuntimeError("Error: NO EMPTY PINS")

	def getPinA(self):
		if self.pinA == None:
			return input("Enter Pin A input for gate" + \
					self.getName() + "-->")
		else:
			return self.pinA.getFrom().getOutput()


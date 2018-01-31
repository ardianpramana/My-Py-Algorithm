'''
Question 5
Level 1

Question:
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

'''

class MagicString(object):
	def __init__(self):
		self.s = ''

	def getString(self):
		self.s = raw_input('input your string: ')

	def printString(self):
		print "you've input ", self.s.upper()

strObj = MagicString()
strObj.getString()
strObj.printString()
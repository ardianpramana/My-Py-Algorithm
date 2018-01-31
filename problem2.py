'''
Question 2
Level 1

Question:
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320
'''

# 2! = 2 * 1
# 3! = 3 * 2 * 1
# 4! = 4 * 3 * 2 * 1

def factorial(x):
	if x == 1:
		print x,
		return x
	else:
		res = x * factorial(x - 1)
		print x,
		return res

print
inp = int(raw_input("Search factorial of: "))
fac = factorial(inp)
print '=', fac
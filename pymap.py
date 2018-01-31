# contain map, filter, reduce

items = range(1,6)	#[1,2,3,4,5]

print items
squared = []
for i in items:
  squared.append(i**2)
print squared

# map implement
squared2 = list(map(lambda x: x**2, items))
print squared2

def multiply(x):
	return(x*x)
def add(x):
	return(x+x)

funcs = [multiply, add]
for i in range(5):
	value = list(map(lambda x: x(i), [multiply,add]))
	value2 = list(map(lambda x: x(i), funcs))
	print value
	print value2

print list(map(add, items))


# filter return value which result True

number_list = range(-5,5)
less_than_zero = list(filter(lambda x: x<0, number_list))
print(less_than_zero)

# without reduce
total = 0
lists = range(1,6)
for num in lists:
	total += num

print total

# with reduce
from functools import reduce
product = reduce((lambda x, y: x + y ), lists)
print product
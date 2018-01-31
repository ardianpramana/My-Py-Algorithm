# lambda argument: manipulate(argument)
add = lambda x, y: x + y
print add(2,4)

square = lambda x: x ** 2
print square(3)

a = [(1,2), (4,1), (9,10), (13,-3)]
print a
a.sort(key=lambda x: x[1])
print a
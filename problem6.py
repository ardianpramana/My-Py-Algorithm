import math

c = 50
h = 30
input_d = raw_input('enter three number separated with comma: ')
print "You've input", input_d

d = input_d.split(',')

result = []
for item in d:
	result.append(str(int(round(math.sqrt(2*c*float(item)/h)))))

print ','.join(result)
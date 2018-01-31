hk = []
hkk = []

for i in range(1,20):
    hk.append(1.0)

print 'list hk ', hk
print 'sum hk ', sum(hk)
print 

inp = 0.5
hk.append(inp)
print 'add ', inp
print 'list hk ', hk
print 'sum hk ', sum(hk)
print

inp = float(raw_input('berapa? '))
print 'add ', inp

# if (sum(hk)+inp) <= 20:
#     hk.append(inp)
#     print 'list hk ', hk
#     print 'sum hk', sum(hk)

# elif (sum(hk)+inp) > 20:
#     print 'cannot add ', inp
#     print 'sum of K/L exceed 20'
#     print 'list hk ', hk
#     hkk.append(inp)
#     print 'list hkk ', hkk

if not ((sum(hk)+inp) > 20):
    hk.append(inp)
    print 'list hk ', hk
    print 'sum hk', sum(hk)

elif not ((sum(hk)+inp) <= 20):
    print 'cannot add ', inp
    print 'sum of K/L exceed 20'
    print 'list hk ', hk
    hkk.append(inp)
    print 'sum hk', sum(hk)
    print 'list hkk ', hkk
    print 'sum hkk', sum(hkk)
print


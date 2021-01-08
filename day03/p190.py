data = input('input 3 numbers')
d = data.split(' ')

print(d)

for n in d:
    print('%s %s' % (n,n.isdecimal()))
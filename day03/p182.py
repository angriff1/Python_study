str = '   python   '
str = str.upper()
print(str)
print(str.lstrip())
print(str.rstrip())
print(str.strip())

s1 = 'a b c d'
s2 = 'a-b-c-d'
r1 = s1.split(' ')
r2 = s2.split('-')
print(type(r1))
print(r1)
print(r2)

for i in r2:
    print(i.strip())

s3 = 'py^th^on'
s4 = s3.replace('^','')
print(s4)
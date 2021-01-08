s = 'python programming'
print(type(s))
print(type(s[0]))

print(len(s))
print(s.find('o'))
print(s.rfind('o'))
print(s.index('r'))
print(s.rindex('r'))
print(s.count('o'))

print('a' in s)
print('a' not in s)

if('a' in s):
    print('OK')
else:
    print('NO')

if s.startswith('p'):
    print('ok')

if s.endswith('g'):
    print('ok')
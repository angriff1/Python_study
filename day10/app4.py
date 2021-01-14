str = '3 + 4 + 5'
strlist = '[1, 2, 3, 4, 5]'

print(eval(str))
print(eval(strlist))

for i in eval(strlist):
    print(i)

users = """[
{'id':'id01', 'name':'james'},
{'id':'id02', 'name':'james'},
{'id':'id03', 'name':'james'}
]"""

for u in eval(users):
    print(u['id'] + ' ' + u['name'])

usersstr = repr(users)
print(usersstr)

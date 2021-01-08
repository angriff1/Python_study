def myfilter(n):
    return n >= 90

def mymap(n):
    return n / 3

score = [93,87,65,100]

"""
for i in score:
    if i >= 90:
        print(i)

for i in filter(myfilter, score):
    print(i)

print('--------------------------')

for i in filter(lambda x:x>=90, score):
    print(i)
"""

for i in map(mymap, score):
    print(i)
print()
for i in map(lambda x:x/3,score):
    print(i)
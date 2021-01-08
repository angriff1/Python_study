list = []
for n in range(1,100,5):
    list.append(n)

print(len(list))

for n in range(1,51):
    if n % 10 == 0:
        print("+",end='')
    else:
        print("-",end='')

for n in range(1,11):
    if n % 2 == 1:
        continue
    print(n)
score = []
score1 = [10,20,30,40,50,60,70,80]
temp = score1[1:5]
print(temp)

sum = 0
for i in score1:
    sum += i
print('Result: %d %10.2f' % (sum,sum/len(score1)))

score2 = [[1,2,3,4],[5,6,7,8],[9,10]]
print('%s\n%s\n%s' % (score2[0],score2[1],score2[2]))

for i1 in score2:
    for i2 in i1:
        print(i2,end=' ')
    print()

total = 0
for i1 in score2:
    sum = 0
    cnt = len(i1)
    for i2 in i1:
        sum += i2
    print('%d %.2f' % (sum,sum/cnt))
    total += sum
print('%d' % total)
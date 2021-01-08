import random

score = (10,20,30,40)
print(type(score))
print(score[0:2])
#score(0) = 99
score = score + (50,60,70)
print(score)

t = []
for i in range(1,7):
    temp = random.randint(1,3)
    t.append(temp)

tp = tuple(t)
print(tp)
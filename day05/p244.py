score = [90,80,60,100]
#score.sort(reverse=True)
score2 = sorted(score,reverse=True)
for i in enumerate(score2,1):
    print(i,sep=' ')
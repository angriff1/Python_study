import random

prize = random.randint(100,10000000000) #상금100~100억 랜덤

buycount = input("몇개 구매?: ")
buycount = int(buycount)
lottonum=[]

answernum = random.sample(range(1,46),7) #당첨번호

for i in range(1,buycount+1): #산 개수만큼 로또 생성
    num = random.sample(range(1,46),7)
    if num not in lottonum:
        lottonum.append(num)


for i in range(len(lottonum)): #산 로또 출력
    print(lottonum[i])
print('=============================')
print('당첨 번호: ',answernum)
print('총 당첨금은?: %d원'% prize)

print('=========분석 시작================')
personcnt=0

firstcnt=0 #1등 개수
secondcnt=0
thirdcnt=0
fourthcnt=0
fifthcnt=0
nothingcnt=0



for i in lottonum:
    anscnt = 0  # 맞은 개수
    for j in i:
        if j in answernum:
            anscnt+=1
    personcnt+=1
    print('%d번째 로또 맞은 개수: %d'% (personcnt,anscnt))
    if anscnt == 7:
        print('     축하! 1등입니다! 상금은 %.2f원 입니다!!' %(prize*0.6))
        firstcnt+=1
        print()
    elif anscnt ==6:
        print('     축하! 2등입니다! 상금은 %.2f원 입니다!!' %(prize*0.2))
        secondcnt += 1
        print()
    elif anscnt ==5:
        print('     축하! 3등입니다! 상금은 %.2f원 입니다!!' %(prize*0.1))
        thirdcnt += 1
        print()
    elif anscnt ==4:
        print('     축하! 4등입니다! 상금은 %.2f원 입니다!!' %(prize*0.05))
        fourthcnt += 1
        print()
    elif anscnt ==3:
        print('     축하! 5등입니다! 상금은 %.2f원 입니다!!' %(prize*0.025))
        fifthcnt+=1
        print()
    else:
        print('     축하! 돈을 내다 버리셨습니다!')
        nothingcnt+=1
        print()

print('당첨된 갯수 파악: 1등 %d개 '%firstcnt)
print('당첨된 갯수 파악: 2등 %d개 '%secondcnt)
print('당첨된 갯수 파악: 3등 %d개 '%thirdcnt)
print('당첨된 갯수 파악: 4등 %d개 '%fourthcnt)
print('당첨된 갯수 파악: 5등 %d개 '%fifthcnt)
print('당첨된 갯수 파악: 꽝  %d개 '%nothingcnt)
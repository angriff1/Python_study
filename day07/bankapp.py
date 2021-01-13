from bankapi import Account

acc1 = Account('1111', 10000, 4.5)
print('잔액은 %d 입니다.' % (acc1.inquire()))
acc1.withdraw(5000)
print('잔액은 %d 입니다.' % (acc1.inquire()))

accList = []
accList.append(Account('1111', 10000, 3.5))
accList.append(Account('2222', 20000, 3.6))
accList.append(Account('3333', 30000, 3.7))
accList.append(Account('4444', 40000, 3.8))
accList.append(Account('5555', 50000, 3.9))

for acc in accList:
    print(acc)

# 잔액 평균과 금리 평균을 구하시오
bsum = 0
rsum = 0.0

for acc in accList:
    bsum += acc.balance
    rsum += acc.rate

print(bsum / len(accList))
print(rsum / len(accList))

print('잔액 평균: %d, 이자 평균: %.2f' % Account.getAvg(accList))
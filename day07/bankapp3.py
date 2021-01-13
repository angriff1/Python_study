import bankapi
from bankapi import Account

acc1 = Account('1111', 10000, 3.4)
print(acc1)
try:
    acc1.withdraw(20000)
except bankapi.MinusMoney:
    print('잔액 부족입니다.')
except bankapi.NotEnoughError:
    print('잔액 부족입니다.')
print(acc1)
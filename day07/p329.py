import math

print(math.cos(3.141592))

class Account:
    def __init__(self, accNo, balance, rate):
        "Constructor"
        self.accNo = accNo
        self.balance = balance
        self.rate = rate
    def deposit(self, money):
        self.balance += money
    def withdraw(self, money):
        self.balance -= money
    def inquire(self):
        return self.balance

acc1 = Account('1111',20000,4.5)
print('잔액은 %d 입니다.' % (acc1.inquire()))

acc1.deposit(10000)
print('잔액은 %d 입니다.' % (acc1.inquire()))


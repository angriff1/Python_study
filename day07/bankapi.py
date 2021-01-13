class Account:
    def __init__(self, accNo, balance, rate):
        "Constructor"
        self.__accNo = accNo
        self.__balance = balance
        self.__rate = rate

    def __str__(self):
        return self.__accNo + ' ' + str(self.__balance) + ' ' + str(self.__rate) + ' ' + str(self.getRateMoney())

    def deposit(self, money):
        self.__balance += money

    def withdraw(self, money):
        if money < 0:
            raise MinusError
        if self.__balance < money:
            raise NotEnoghError
        self.__balance -= money

    def inquire(self):
        return self.__balance

    def getAvg(accList):
        bsum = 0
        rsum = 0.0
        for acc in accList:
            bsum += acc.__balance
            rsum += acc.__rate
        return bsum/len(accList), rsum/len(accList)

    def getRateMoney(self):
        m = 0
        m = self.__balance * self.__rate * 0.01
        return m

    def getRate(self):
        return self.__rate

    def setRate(self, rate):
        self.__rate = rate

class NotEnoghError(Exception):
    """Inappropriate argment value (of correct type)."""
    def __init__(self, *args, **kwargs): # real signature unkown
        pass

class MinusError(Exception):
    """Inappropriate argment value (of correct type)."""
    def __init__(self, *args, **kwargs): # real signature unkown
        pass
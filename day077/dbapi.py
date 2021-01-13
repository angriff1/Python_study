class Order():
    def __init__(self, ordernum, price, username, item, status):
        # num = 0
        self.__ordernum = ordernum
        self.__price = price
        self.__username = username
        self.__item = item
        self.__status = status

    # @classmethod
    # def numCount(cls):
    #     cls.num += 1

    def __str__(self):
        return '주문 번호: ' + self.__ordernum + \
               '  가격: ' + str(self.__price) + \
               '  성명: ' + self.__username + \
               '  품목: ' + self.__item + \
               '  상태: ' + self.__status

    def sqlmap(self):
        return self.__ordernum, self.__price, self.__username, self.__item, self.__status

    def getOrdernum(self):
        return self.__ordernum

    def setOrdernum(self, ordernum):
        self.__ordernum = ordernum

    def getPrice(self):
        return self.__price

    def setPrice(self, price):
        if price <= 0:
            raise ValueError
        self.__price = price

    def getUsername(self):
        return self.__username

    def setUsername(self, username):
        self.__username = username

    def getItem(self):
        return self.__item

    def setItem(self, item):
        self.__item = item

    def getStatus(self):
        return self.__status

    def setStatus(self, status):
        self.__status = status

    ordernum = property(getOrdernum)
    price = property(getPrice, setPrice)
    username = property(getUsername)
    item = property(getItem, setItem)
    status = property(getStatus, setStatus)

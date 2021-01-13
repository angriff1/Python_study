import sqlite3
from dbapi import Order

class Sql:
    dropOrdertb = "DROP TABLE IF EXISTS ordertb"
    makeOrdertb = """CREATE TABLE IF NOT EXISTS ordertb (
                ordernum CHAR(12) PRIMARY KEY,
                price NUMBER(6),
                username CHAR(12),
                item CHAR(20),
                status CHAR(12)
                )"""
    insertOrder = "INSERT INTO ordertb VALUES ('%s', %d, '%s', '%s', '%s')"
    selectAllOrder = "SELECT * FROM ordertb"
    selectOneOrder = "SELECT * FROM ordertb WHERE ordernum = '%s'"
    deleteOrder = "DELETE FROM ordertb WHERE ordernum = '%s'"
    updateOrder = "UPDATE orders SET %s %s %s %s WHRERE ordernum = '%s'"

class SqliteDb:
    def __init__(self, dbName):
        self.__dbName = dbName

    def connectDb(self):
        "Connect SQLite"
        con = sqlite3.connect(self.__dbName)
        cursor = con.cursor()
        return {'con':con, 'cursor':cursor}

    def closeDb(self, cc):
        if cc['cursor'] != None:
            cc['cursor'].close()
        if cc['con'] != None:
            cc['con'].close()

    def dropTable(self):
        "Drop order table"
        cc = self.connectDb()
        cc['cursor'].execute(Sql.dropOrdertb)
        cc['con'].commit()
        self.closeDb(cc)

    def makeTable(self):
        "Make order table"
        cc = self.connectDb()
        cc['cursor'].execute(Sql.makeOrdertb)
        cc['con'].commit()
        self.closeDb(cc)

    def insert(self, order):
        "Insert an order data"
        cc = self.connectDb()
        cc['cursor'].execute(Sql.insertOrder % order.sqlmap())
        cc['con'].commit()
        self.closeDb(cc)

    def select(self):
        "Select order data"
        cc = self.connectDb()
        cc['cursor'].execute(Sql.selectAllOrder)
        result = cc['cursor'].fetchall()
        allorders = []
        for o in result:
            order = Order(o[0], o[1], o[2], o[3], o[4])
            allorders.append(order)
        self.closeDb(cc)
        return allorders

    def selectOne(self, ordernum):
        "Select an order"
        cc = self.connectDb()
        cc['cursor'].execute(Sql.selectOneOrder % ordernum)
        o = cc['cursor'].fetchone()
        order = Order(o[0], o[1], o[2], o[3], o[4])
        self.closeDb(cc)
        return order

    def delete(self, ordernum):
        "Delete an order"
        cc = self.connectDb()
        cc['cursor'].execute(Sql.deleteOrder % ordernum)
        self.closeDb(cc)

    def update(self, order):
        "Update an order"
        cc = self.connectDb()
        cc['cursor'].execute(Sql.updateOrder % order.sqlmap())
        cc['con'].commit()
        self.closeDb(cc)
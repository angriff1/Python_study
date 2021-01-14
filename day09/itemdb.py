from sqlitedb import *

class ItemDb(SqliteDb):
    def __init__(self, dbName):
        super().__init__(dbName)

    def insert(self, i):
        cc = self.getConnect()
        cc['cursor'].execute(Sql.insertItem % i.sqlmap())
        cc['con'].commit()
        self.close(cc)

    def delete(self, id):
        cc = self.getConnect()
        cc['cursor'].execute(Sql.deleteItem % id)
        cc['con'].commit()
        self.close(cc)

    def update(self, i):
        cc = self.getConnect()
        cc['cursor'].execute(Sql.updateItem % (i.name, i.price, i.id))
        cc['con'].commit()
        self.close(cc)

    def select(self):
        cc = self.getConnect()
        cc['cursor'].execute(Sql.selectAllItem)
        result = cc['cursor'].fetchall()
        all = []
        for ii in result:
            obj = Item(ii[0], ii[1], ii[2])
            all.append(obj)
        self.close(cc)
        return all

    def selectone(self, id):
        cc = self.getConnect()
        cc['cursor'].execute(Sql.selectItem % id)
        obj = cc['cursor'].fetchone()
        result = Item(obj[0], obj[1], obj[2])
        self.close(cc)
        return result
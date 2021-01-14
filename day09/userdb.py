from sqlitedb import *

class UserDb(SqliteDb):
    def __init__(self, dbName):
        super().__init__(dbName)

    def insert(self, u):
        cc = self.getConnect()
        cc['cursor'].execute(Sql.insertUser % u.sqlmap())
        cc['con'].commit()
        self.close(cc)

    def delete(self,id):
        cc = self.getConnect()
        cc['cursor'].execute(Sql.deleteUser % id)
        cc['con'].commit()
        self.close(cc)

    def update(self, u):
        cc = self.getConnect()
        cc['cursor'].execute(Sql.updateUser % (u.pwd, u.name, u.age, u.id))
        cc['con'].commit()
        self.close(cc)

    def select(self):
        cc = self.getConnect()
        cc['cursor'].execute(Sql.selectAllUser)
        result = cc['cursor'].fetchall()
        all = []
        for ii in result:
            obj = User(ii[0], ii[1], ii[2], ii[3])
            all.append(obj)
        self.close(cc)
        return all

    def selectone(self, id):
        cc = self.getConnect()
        cc['cursor'].execute(Sql.selectUser % id)
        uu = cc['cursor'].fetchone()
        us = User(uu[0],uu[1],uu[2],uu[3])
        self.close(cc)
        return us
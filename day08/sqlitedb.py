import sqlite3
from value import user

class Sql:
    makeusertb = """CREATE TABLE IF NOT EXISTS usertb(
                    id CHAR(10) PRIMARY KEY,
                    pwd  CHAR(10),
                    name CHAR(10),
                    age  NUMBER(3)
    )"""
    insertUser = """INSERT  INTO  usertb VALUES ('%s','%s','%s',%d)"""
    deleteUser = """DELETE  FROM   usertb  WHERE  id = '%s'"""
    updateUser = """UPDATE  usertb  SET  pwd='%s', name='%s', age=%d  WHERE  id='%s'"""
    selectUser = """SELECT  *  FROM  usertb   WHERE  id='%s'"""
    selectAllUser = """SELECT  *  FROM  usertb"""

class SqliteDb:
    def __init__(self, dbName):
        self.__dbName = dbName
    def getConnect(self):
        con = sqlite3.connect(self.__dbName)
        cursor = con.cursor()
        #print(self.__dbName+ ' Connected ...')
        return {'con':con, 'cursor':cursor}

    def close(self, cc):
        if cc['cursor'] != None:
            cc['cursor'].close()
        if cc['con'] != None:
            cc['con'].close()

    def makeTable(self):
        "Make usertb Table"
        cc = self.getConnect()
        cc['cursor'].execute(Sql.makeusertb)
        cc['con'].commit()
        self.close(cc)

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
        userall = []
        for u in result:
            # ('','','',20)
            tu = user(u[0],u[1],u[2],u[3])
            userall.append(tu)
        self.close(cc)
        return userall

    def selectone(self, id):
        cc = self.getConnect()
        cc['cursor'].execute(Sql.selectUser % id)
        #('','','',39)
        uu = cc['cursor'].fetchone()
        us = user(uu[0],uu[1],uu[2],uu[3])
        self.close(cc)
        return us

import sqlite3
from value import *

class Sql:
    makeusertb = """CREATE TABLE IF NOT EXISTS usertb(
                    id CHAR(10) PRIMARY KEY,
                    pwd  CHAR(10),
                    name CHAR(10),
                    age  NUMBER(3)
                )"""
    makeitemtb = """CREATE TABLE IF NOT EXISTS itemtb(
                    id CHAR(10) PRIMARY KEY,
                    name CHAR(10),
                    price NUMBER(10)
                )"""
    insertUser = "INSERT  INTO  usertb VALUES ('%s', '%s', '%s', %d)"
    deleteUser = "DELETE  FROM   usertb  WHERE  id = '%s'"""
    updateUser = "UPDATE  usertb  SET  pwd='%s', name='%s', age=%d  WHERE  id='%s'"
    selectUser = "SELECT  *  FROM  usertb   WHERE  id='%s'"
    selectAllUser = "SELECT  *  FROM  usertb"

    insertItem = "INSERT  INTO  itemtb VALUES ('%s', '%s', %d)"
    deleteItem = "DELETE  FROM   itemtb  WHERE  id = '%s'"
    updateItem = "UPDATE  itemtb  SET  name='%s', price=%d  WHERE  id='%s'"
    selectItem = "SELECT  *  FROM  itemtb   WHERE  id='%s'"
    selectAllItem = "SELECT  *  FROM  itemtb"

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
        cc['cursor'].execute(Sql.makeitemtb)
        cc['con'].commit()
        self.close(cc)

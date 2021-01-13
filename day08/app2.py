from sqlitedb import *;
from value import *;

sqlitedb = SqliteDb('udb.db');

userlist = sqlitedb.select();
for u in userlist:
    print(u);

us = user('id01','1111','kim',30);
sqlitedb.update(us);
print('-------------------------------------');

userlist = sqlitedb.select();
for u in userlist:
    print(u);
from sqlitedb import *;
from value import *;

print('start ....');

sqldb = SqliteDb('udb.db');
sqldb.makeTable();
u = user('id05','pwd05','james',28);
#sqldb.insert(u);
userlist = sqldb.select();
for us in userlist:
    print(us.id+' '+us.name+' '+str(us.age));
print('---------------------------------');
userone = sqldb.selectone('id01');
print(userone);

sqldb.delete('id02');
userlist = sqldb.select();
for us in userlist:
    print(us.id+' '+us.name+' '+str(us.age));
print('---------------------------------');

print('end ....');
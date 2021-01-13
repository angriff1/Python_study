from dbutil import *
from dbapi import Order


# 1. SQLite에 접속한다.
sqldb = SqliteDb('order.db')
#print('SQLite connected')
sqldb.dropTable()
#print('Table dropped')

# 2. Table을 생성한다.
sqldb.makeTable()
#print('Table created')

# 3. 주문 정보를 입력한다.
order1 = Order('001', 10000, '이말숙', 'item01', '준비중')
sqldb.insert(order1)
#print(order1)
order2 = Order('002', 20000, '김말숙', 'item02', '배송중')
sqldb.insert(order2)
#print(order2)
order3 = Order('003', 30000, '박말숙', 'item03', '배송중')
sqldb.insert(order3)

# 4. 주문 정보를 조회한다.
allorders = sqldb.select()
print('=====================   주   문   목   록   ====================')
for order in allorders:
    print(order)
    #print(type(order))
    #print(dbapi.Order(order))
print('===============================================================')

order = sqldb.selectOne('002')
print(order)

#SqliteDb.updateOrder('001', item = 'item03')
#print('Order updated')

#print('Error')
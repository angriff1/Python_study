import dbutil

print('start')
con = None
cursor = None

try:
    # 1. SQLite에 접속한다.
    dbutil.connectDB('addr.db')
    print('SQLite Connected')

    # 2. Table을 생성한다.
    dbutil.makeTable()
    print('Table created')

    # 3. 사용자 정보를 입력한다.
    user = ['id06', 'pwd06', '홍말숙', '01077776666', '경기', 20]
    dbutil.insertUser(user)

    # 4. 사용자 정보를 조회한다.
    allusers = dbutil.selectUser()
    for user in allusers:
        print('%s %s %s %s %s %d' % (user[0], user[1], user[2], user[3], user[4], user[5]))
except:
    print('Error')



finally:
    # 5. SQLite를 close 한다.
    dbutil.closeDB()

print('end')
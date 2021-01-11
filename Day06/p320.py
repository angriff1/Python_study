import sqlite3

print('start')
con = None
cursor = None

# 1. SQLite에 접속한다.
con = sqlite3.connect('addr.db')
cursor = con.cursor()
print('SQLite Connected')

# 2. Table을 생성한다.
#cursor.execute('DROP TABLE IF EXISTS users')
cursor.execute("""CREATE TABLE IF NOT EXISTS users (
	id	CHAR(16) PRIMARY KEY,
	pwd	CHAR(16),
	name	CHAR(10),
	phone	CHAR(15),
	addr	CHAR(20),
	age	NUMBER(3)
) """)
con.commit()
print('Table created')

# 3. 사용자 정보를 입력한다.
cursor.execute("""INSERT INTO users VALUES
('id03','pwd03','이말숙','01099992222','서울',29)""")
con.commit()

# 4. 사용자 정보를 조회한다.
cursor.execute('SELECT * FROM users')
allusers = cursor.fetchall()
for user in allusers:
    print('%s %s %s %s %s %d' % (user[0], user[1], user[2], user[3], user[4], user[5]))

# 5. SQLite를 close 한다.
cursor.close()
con.close()

print('end')
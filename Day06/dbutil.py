import sqlite3

con = None
cursor = None

def connectDB(dbName):
    "Connect SQLite"
    global con, cursor
    con = sqlite3.connect(dbName)
    cursor = con.cursor()

def makeTable():
    "Make users Table"
    cursor.execute("""
        create table if not exists users (
            id CHAR(16) primary key,
            pwd CHAR(16),
            name CHAR(10),
            phone CHAR(15),
            addr CHAR(20),
            age NUMBER(3));
        """);
    print('Table Created..')


def insertUser(user):
    "Insert user data"
    global con, cursor
    insertSQL = """INSERT INTO users VALUES ('%s','%s','%s','%s','%s',%d)""" % \
                (user[0], user[1], user[2], user[3], user[4], user[5])
    cursor.execute(insertSQL)
    con.commit()

def selectUser():
    "Select user data"
    allusers = []
    selectSQL = """SELECT * FROM users"""
    users = cursor.execute(selectSQL)
    for u in users:
        user = []
        for i in u:
            if i.isdecimal():
                i = int(i)
            user.append(i)
        allusers.append(user)
    return allusers


def selectOneUser(id):
    "Select a user"
    user = []
    selectOneSQL = """SELECT * FROM users WHERE id = %s""" % (id)
    cursor.execute(selectOneSQL)
    userData = cursor.fetchone()
    user.append(userData[0])
    user.append(userData[1])
    user.append(userData[2])
    user.append(userData[3])
    user.append(userData[4])
    user.append(userData[5])
    return user

def deleteUser(id):
    "Delete a user"
    deleteSQL = """DELETE FROM users WHERE id = '%s'""" % (id)
    cursor.execute(deleteSQL)
    con.commit()

def updateUser(user):
    "Update a user"
    updateSQL = """ UPDATE users SET pwd = '%s', name = '%s', phone = '%s', addr = '%s', age = %d, WHERE id = '%s'""" \
                % (user[1], user[2], user[3], user[4], user[5], user[0])
    cursor.execute(updateSQL)
    con.commit()

def closeDB():
    "Close SQLite"
    global con, cursor
    if cursor != None:
        cursor.close()
    if con != None:
        con.close()

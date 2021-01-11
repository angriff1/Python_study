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


def insertUser(user):
    "Insert user data"
    global con, cursor
    insertSQL = """INSERT INTO users VALUES ('%s','%s','%s','%s','%s',%d)""" % \
                (user[0], user[1], user[2], user[3], user[4], int(user[5]))
    cursor.execute(insertSQL)
    con.commit()

def selectUser():
    "Select user data"
    global con, cursor
    allusers = []
    selectSQL = """SELECT * FROM users"""
    users = cursor.execute(selectSQL)
    for u in users:
        user = []
        for i in u:
            user = []
            if i.isdecimal():
                i = int(i)
            user.append(i)
        allusers.append(user)
    return allusers


def selectOneUser(id):
    "Select a user"
    global con, cursor
    user = None
    selectOneSQL = """SELECT * FROM users WHERE id%d""" % (id)

    return user


    return user

def deleteUser(id):
    "Delete a user"
    global con, cursor
    deleteSQL = """DELETE FROM users WHERE id = '%s'""" % (id)
    cursor.execute(deleteSQL)
    con.commit()

def updateUser(user):
    "Update a user"
    global con, cursor
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
import sqlite3
import dbutil

try:
    dbutil.connectDB('addr.db')
    while True:
        menu = input('Input menu(c,r,ro,u,d,q) : ')
        if menu == 'q':
            dbutil.closeDB()
            break
        if menu == 'c':
            smenu = input('Input user data : ')
            userdata = smenu.split(' ')
            userdata[5] = int(userdata[5])
            dbutil.insertUser(userdata)
        if menu == 'r':
            allusers = dbutil.selectUser()
            for user in allusers:
                print('%s %s %s %s %s %d' % (user[0], user[1], user[2], user[3], user[4], user[5]))
        if menu == 'ro':
            smenu = input('Input user ID : ')
            user = dbutil.selectOneUser(smenu)
            for i in user:
                print(i, end = ' ')
            print()
        if menu == 'u':
            smenu = input('Input user data : ')
            userdata = smenu.split(' ')
            userdata[5] = int(userdata[5])
            dbutil.updateUser(userdata)
        if menu == 'd':
            smenu = input('Input user ID : ')
            dbutil.deleteUser(smenu)
except:
    print('Error')
finally:
    dbutil.closeDB()
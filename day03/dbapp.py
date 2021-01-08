import dbutil

print('start')
while True:
    menu = input('Input menu ... [i,s,sa,q]')
    if menu == 'q':
        print('bye')
        break
    if menu == 'i':
        data = input('Input information..')
        data = data.split(' ')
        dbutil.insert(id=data[0].strip(),
                      pwd=data[1].strip(),
                      name=data[2].strip(),
                      age=int(data[3].strip()))
    if menu == 'sa':
        users = dbutil.selectall() # list안에 list
        # 출력
        for user in users:
            print('User Info %s %s %s %d' % (user[0],user[1],user[2],user[3]))

    if menu == 's':
        inputid = input('input user id ..')
        user = dbutil.select(id=inputid)
        print('User Info %s %s %s %d' % (user[0],user[1],user[2],user[3]))

print('end')
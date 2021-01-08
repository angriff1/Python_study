def insert(**a):
    id = a['id']
    pwd = a['pwd']
    name = a['name']
    age = a['age']
    print('%s %s %s %d inserted .....' % (id,pwd,name,age))

def select(**a):
    id = a['id']
    data = []
    data.append('id01')
    data.append('pwd01')
    data.append('이말숙')
    data.append(25)
    return data

def selectall():
    data = []
    data.append(['id01','pwd01','이말숙',25])
    data.append(['id02','pwd02','김말숙',26])
    data.append(['id03','pwd03','황말숙',27])
    data.append(['id04','pwd04','정말숙',28])
    data.append(['id05','pwd05','장말숙',29])
    return data
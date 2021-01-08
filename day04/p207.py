def error():
    print('wrong input... try again\n')

def searchcart(cart,itemname):
    for i in cart:
        if i[0] == itemname:
            print(i)
            return i
    print('no item')
    return 0

def insertcart(cart):
    while True:
        item = input('Input Item(name,price,count)')
        item = item.split(' ')
        if len(item) == 3:
            if searchcart(cart,item[0]) != 0:
                print('This item name is already in cart!')
                continue
            if item[1].isdecimal() and item[2].isdecimal():
                item[1] = int(item[1])
                item[2] = int(item[2])
                cart.append(item)
                break
        error()

def viewcart(cart):
    ptotal = 0
    ctotal = 0
    for i in cart:
        print('Item: %s %d %d' % (i[0], i[1], i[2]))

def removecart(cart):
    item = input('Input Item name')


print('start')
#data = [['item1',1000,1],['item2',2000,1],['item3',3000,1]]
cart = []

while True:
    menu = input('Input menu(i,v,r,q)')
    if menu == 'i':
        insertcart(cart)
    if menu == 'v':
        viewcart(cart)
    if menu == 'd':
        removecart(cart)
    if menu == 'q':
        print('bye')
        break
print('end')


def calcsum(n):
    sum = 0
    for d in n:
        sum += d
    return sum

def f1():
    data = 100
    return data

def f2(s,e):
    sum = 0
    for data in range(s,e+1):
        sum += data
    return sum / (e-s+1)

def f3(a,b):
    sum = a+b
    return sum


def f4(*n):
    sum = 0
    for d in n:
        sum += d
    return sum

def f5(m,*n):
    sum = 0
    for d in n:
        sum += d
    return sum +m

def f6(begin=1,end=2,step=1):
    """ begin:start data ... default value = 1
    """
    sum = 0
    for d in range(begin,end+1,step):
        sum == d
    return sum

def f7(**args):
    b = args['b']
    e = args['e']
    s = args['s']
    sum = 0
    for d in range(b,e+1,s):
        sum == d
    return sum

def f8(n,*m,**a):
    print('TEST')
    print(n)
    print(m)
    print(a)
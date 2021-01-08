import myutil1

def sum(a,b):
    result = a + b
    return result

def calc(n):
    if n == 0:
        raise ZeroDivisionError
    result = 10 / n
    return result

d = 0
try:
    result = calc(d)
    print(result)
except:
    print('숫자가 잘못 입력 되었습니다.')

d = 1000
try:
    result = myutil1.input(d)
    print('입력금액은 %d 입니다.' % result)
except:
    print('숫자가 잘못 입력 되었습니다.')
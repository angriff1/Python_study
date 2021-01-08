print('start............')
while True:
    data = input('input number..?[q:quit]')
    if data.lower() == 'q':
        print('bye..')
        break
    if data.isdecimal():
        result = int(data) * 1000
        print(result)
    else:
        print('invaild number type.. try again')

# data.isalnum() 숫자 또는 문자냐
print('end.......')
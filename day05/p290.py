d = 'a'
result = 0
try:
    num = int(d)
    result = 10 /num
except ValueError as e:
    print('Invalid input character')
    exit()
except ZeroDivisionError:
    print('')
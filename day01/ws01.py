print("start")
a = input('input a number 1 : ')
b = input('input a number 2 : ')
c = input('input a number 3 : ')
try:
    a = int(a)
    b = int(b)
    c = int(c)
except:
    print("Invalid input number... Try again")
    exit()

sum = a+b+c
print(sum)
print(round(sum/3, 1))

print("end")
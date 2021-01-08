a = input('input a number : ')
b = input('input a number : ')
c = input('input a number : ')
try:
    num1 = int(a)
    num2 = int(b)
    num3 = int(c)
except:
    print("Invalid input number... Try again")
    exit()

sum = num1 + num2 + num3
avg = round(sum/3, 1)
print(sum)
print(avg)
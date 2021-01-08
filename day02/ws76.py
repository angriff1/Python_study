# Get a number in range 1~9
num = input('Input a number in range 1~9 : ')

# If not in range or number, exit program
try:
    num = int(num)
except:
    print('# Error! It is not integer')
    exit()
if num < 1 or num > 9:
    print('# Error! It is not in range')
    exit()

# Sum and average
sum = 0
for i in range(1,num+1):
    sum = sum + i
print(sum)
print(sum/num)  # averagez
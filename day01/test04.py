# 숫자를 입력 받는다.
a = input('input number : ')
num = 0
try:
    num = int(a)
except:
    print("Invalid input number... Try again")
    exit()

# 1에서 입력 받은 숫자 만큼 출력 한다.
# 합과 평균을 최정적으로 출력하시오.
sum = 0
for i in range(1,num+1) :
    print(i)
    sum = sum + i
avg = sum/num
print(sum)
print(avg)
data = [98,87,90,34,56,43]

# 1. 위 데이터의 합과 평균을 구하시오
# 2. A ~ F 학점을 출력하시오
sum = 0
for n in data:
    sum += n
avg = sum / len(data)
print(sum)
print(avg)

for n in data:
    if n >= 90:
        print("A", end=" ")
    elif n >= 80:
        print("B", end=" ")
    elif n >= 70:
        print("C", end=" ")
    elif n >= 60:
        print("D", end=" ")
    else:
        print("F", end=" ")
print("")



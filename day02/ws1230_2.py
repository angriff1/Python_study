data = [
    [100,90,98,88],
    [100,90,98,87],
    [100,90,98,86],
    [100,90,98,95]
]

# 1. 각 학생의 합과 평균을 출력
# 2. 전체 학생의 합과 평균을 출력
sum = []
avg = []
for m in range(0,len(data)):
    sum_arg = 0
    for n in data[m]:
        sum_arg += n
    avg_arg = sum_arg / len(data[m])
    sum.append(sum_arg)
    avg.append(avg_arg)
print(sum)
print(avg)

sum_t = 0
for n in sum:
    sum_t += n
avg_t = sum_t/len(data)
print("전체 합계 : ", sum_t, "| 전체 평균 : ", avg_t)
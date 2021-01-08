import p140

data = [1,2,3,4,5]
result = p140.calcsum(data)

print(result)

result2 = p140.f1()
print(result2)

result3 = p140.f2(2,9)
print(str(result3)+'%')

p140.f3(4,9)
result4 = p140.f4(1,2,3,4,5)
print(result4)

result5 = p140.f5(100, 1,2,3,4,5)
print(result5)

result6 = p140.f6(step=1,end=100,begin=2)
print(result6)

help(p140.f6)

result6 = p140.f7(s=1,e=100,b=2,r=1)
print(result6)

p140.f8('datas',1,2,3,4,5,start=10,end=100)
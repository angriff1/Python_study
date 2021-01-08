gender = input("input gender(m/f) : ")
height = float(input("input height(cm) : "))/100
weight = float(input("input weight(kg) : "))

BMI = weight/(height**2)

if BMI >= 30:
    print("고도비만")
elif BMI >= 25:
    print("비만")
else:
    print("정상")
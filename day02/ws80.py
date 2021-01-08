# Input 4 scores
score1 = input("Input score1 : ")
score2 = input("Input score2 : ")
score3 = input("Input score3 : ")
score4 = input("Input score4 : ")
score = [int(score1), int(score2), int(score3), int(score4)]

# sum & average
sum = 0
for i in score:
    sum = sum + i
avg = sum/len(score)

# Result of score
if avg >= 90:
    print("A")
elif avg >= 80:
    print("B")
elif avg >= 70:
    print("C")
elif avg >= 60:
    print("D")
else:
    print("F")

    # https://colorscripter.com
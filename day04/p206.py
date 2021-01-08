s = []
s.append(20)
s.append(30)
s.append(10)
s.append(40)
s.append(50)
del s[3]
s[1:3] = [1,2,3]
s = s + [9,8,7]
s = s + 3
print(s)
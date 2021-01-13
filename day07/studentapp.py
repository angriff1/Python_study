import studentapi
from studentapi import Human, Student

human = Human('james', 20)
print(human)
print('이름: %s, 나이: %s' % human.print())

st1 = Student('kim', 25, 'EN')
print(st1)
print(st1.study())
print('이름: %s, 나이: %s, 전공: %s' % st1.print())
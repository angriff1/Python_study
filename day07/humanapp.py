import humanapi
from humanapi import Human

human = Human('id01', 'james', 3000)
print(human)

human.setSalary(-5000)
human.salary = 4000

print(human.salary)

human._Human__salary = 1000000
print(human.getSalary())
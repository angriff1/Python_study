num = 100
print('result: '+str(num)+' won')

str1 = 'result:'
str2 = 'won'
print('%s %d %s' % (str1,num,str2))

print('%10d%%' % num)
print()
nums1 = [1000,2000,30,210000]
for n in nums1:
    print('Price: %-10d Won' % n)
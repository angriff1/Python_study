st = [
    {'id':'st1','ko':90,'en':100,'ma':99},
    {'id':'st2','ko':91,'en':90,'ma':98},
    {'id':'st3','ko':92,'en':91,'ma':97}
]

for sts in st:
    print('%s 학생의 평균 %.2f' % ((sts.get('id'),(sts.get('ko')+sts.get('en')+sts.get('ma'))/3)))

kosum = 0; ensum = 0; masum = 0;

for sts in st:
    kosum += sts.get('ko')
    ensum += sts.get('en')
    masum += sts.get('ma')
cnt = len(st)
print('과목별 평균 %.2f %.2f %.2f' % (kosum/cnt, ensum/cnt, masum/cnt))
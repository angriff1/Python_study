f = None
try:
    f = open('live.txt', 'rt', encoding='UTF-8')
    while True:
        text = f.readline()
        if not text:
            break
        print(text)
except:
    print('File not found')
finally:
    if f != None:
        print('close')
        f.close()

"""
f = None
try:
    f = open('live.txt', 'rt', encoding='UTF-8')
    for text in f:
        print(text, end = '')
except:
    print('File not found')
finally:
    if f != None:
        print('close')
        f.close()
"""
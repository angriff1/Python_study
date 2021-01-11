f = None
try:
    f = open('live.txt', 'rt', encoding='UTF-8')
    text = f.read()
    print(text)
except:
    print('File not found')
finally:
    if f != None:
        print('close')
        f.close()
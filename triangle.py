import yogi
n = yogi.read(int)
a = 0
for i in range(n):
    a = i
    while a >= 0:
        print ("*" , end = '')
        a = a - 1
    print ()


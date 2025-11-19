import yogi
a = yogi.read(int)
b = yogi.read(int)
if (a == b):
    print (a)
elif a < b:
    print (a , end = '')
    while a < b:
        a = a + 1
        print ("," , a , sep = '' , end = '')
    print ()
else:
    print ()

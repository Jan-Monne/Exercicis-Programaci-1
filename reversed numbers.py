import yogi
n = yogi.read(int)
q = n
r = 0
if n == 0:
    print (n)
else:
    while q != 0:
        r = q%10
        q = q // 10
        print (r , end = '')
    print ()

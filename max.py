import yogi
a = yogi.read(int)
b = yogi.read(int)
c = yogi.read(int)
if a <= c and b <= c:
    print (c)
elif b <= a and c <= a:
    print (a)
else:
    print (b)

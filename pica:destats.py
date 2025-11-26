import yogi
a = yogi.scan(int)
b = yogi.scan(int)
c = yogi.scan(int)
peak = False
while c != 0:
    if b > 3143 and b > a and b > c:
        peak = True
    a = b
    b = c
    c = yogi.read(int)
if peak:
    print ("YES")
else:
    print ("NO")
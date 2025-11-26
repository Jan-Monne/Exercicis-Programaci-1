import yogi
a = yogi.scan(int)
b = yogi.scan(int)
while a is not None:
    mix = ''
    while a != 0:
        mix = str(a%2) + str(b%2) + mix
        a = a//2
        b = b//2
    print (mix)
    a = yogi.scan(int)
    b = yogi.scan(int)
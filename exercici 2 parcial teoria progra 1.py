import yogi
n = yogi.read(int)
if n == 0:
    print(True)
else:
    d0 = n % 10
    while n != 0:
        dk = n % 10
        n = n // 10
    print (d0 == dk)

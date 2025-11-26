import yogi
n = yogi.read(int)
position = 1
if n > 0:
    x = yogi.scan(int)
    while x != -1 and position <= n:
        if position == n:
            print ("At the position", n , "there is a(n)", x, end = '')
            print (".")
        position += 1
        x = yogi.scan(int)
    if x == -1 and position <= n:
        print ("Incorrect position.")
else:
    print ("Incorrect position.")
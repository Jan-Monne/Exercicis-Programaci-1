import yogi

d = yogi.scan(int)
while d is not None:
    m = yogi.read(int)
    a = yogi.read(int)
    t = False
    data = False
    if (d < 1 or m < 1 or m > 12):
        data = False
    else:
        if ((a%4) == 0):
            if ((a%100) != 0):
                t = True
            else:
                if (((a//100)%4) == 0):
                    t = True
        if m == 2:
            if t and  d <= 29:
                data = True
            elif not(t) and d <= 28:
                data = True
        if m == 4 or m == 6 or m == 9 or m == 11:
            if d <= 30:
                data = True
        elif m != 2:
            if d <= 31:
                data = True
    if data:
        print ("Correct Date")
    else:
        print ("Incorrect Date")
    d = yogi.scan(int)

import yogi
n = yogi.scan(int)
line = 1
ordre = False
if n == 0:
    print("The first line in increasing order is 1.")
else:
    while n is not None and ordre == False:
        ordre = True
        if n == 1:
            ordre = True
        else:
            a = yogi.read(str)
            b = yogi.read(str)
            if ordre:
                if a>b:
                    ordre = False
            for i in range (n-2):
                a = b
                b = yogi.read(str)
                if ordre:
                    if a > b:
                        ordre = False
            n = yogi.scan(int)
        line += 1
    if ordre:
        print("The first line in increasing order is", line-1, end = '')
        print (".")
    else:
        print("There is no line in increasing order.")
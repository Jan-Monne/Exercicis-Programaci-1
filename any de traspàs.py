import yogi
n = yogi.read(int)
if ((n%4) == 0):
    if ((n%100) != 0):
        print ("YES")
    else:
        if (((n//100)%4) == 0):
            print ("YES")
        else:
            print ("NO")
else:
    print ("NO")

import yogi
if __name__ == "__main__":
    a1 = yogi.read(int)
    b1 = yogi.read(int)
    a2 = yogi.read(int)
    b2 = yogi.read(int)
    if (b1<a2 or b2<a1):
        print ("[]")
    elif (a1<=a2 and b1<=b2):
        print ("[" + str(a2) + "," + str(b1) + "]")
    elif (a1<=a2 and b2<=b1):
        print ("[" + str(a2) + "," + str(b2) + "]")
    elif (a2<=a1 and b2<=b1):
        print ("[" + str(a1) + "," + str(b2) + "]")
    elif (a2<=a1 and b1<=b2):
        print ("[" + str(a1) + "," + str(b1) + "]")

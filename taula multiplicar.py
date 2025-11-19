import yogi
if __name__ == "__main__":
    n = yogi.read(int)
    i = 1
    a = 0
    while i<11:
        a = int(a)
        n = int(n)
        a = n*i
        print (str(n) + "*" + str(i) , "=" , str (a))
        i = int(i)
        i = i + 1

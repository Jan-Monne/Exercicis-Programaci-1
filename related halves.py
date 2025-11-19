import yogi
n = yogi.read(int)
ncopy = n
ndig = 0
if n == 0:
    print ("nothing")
else:
    while ncopy > 0:
        ncopy = ncopy//10
        ndig = ndig + 1
    if ndig % 2 == 0:
        x = 0
        y = 0
        halfdig = ndig//2
        for i in range (halfdig):
            y = y + (n%10)
            n = n//10
        for i in range (halfdig):
            x = x + (n%10)
            n = n//10
        if x < y:
            print (x , "<" , y)
        elif x > y:
            print (x , ">" , y)
        else:
            print (x , "=" , y)
    else:
        print ("nothing")

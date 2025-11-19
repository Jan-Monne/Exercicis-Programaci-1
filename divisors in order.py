import yogi
import math
x = yogi.scan(int)
while x is not None:
    arrel = int(math.sqrt(x))
    llista1 = ""
    llista2 = ""
    if x == 1:
        llista1 = "1"
    else:
        for i in range(1, arrel+1):
            if x%i == 0:
                llista1 += str(i) + " "
                if i != x//i:
                    if i != 1:
                        llista2 = str(x//i) + " " + llista2
                    else:
                        llista2 = str(x//i)
    print ("divisors of " + str(x) + ": " , end = '')
    print (llista1 + llista2)
    x = yogi.scan(int)
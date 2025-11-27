import yogi
import math
n = yogi.read(int)
for i in range(n):
    prime = True
    x = yogi.read(int)
    root = int(math.sqrt(x))
    senar = False
    if x%2 != 0:
        senar = True
        for j in range (3, root+1, 2):
            if x%j == 0 and prime:
                prime = False
                break 
    if (prime and senar and x>2):
        print(x, "is prime")
    elif x == 2:
        print(x, "is prime")
    else:
        print(x,"is not prime")

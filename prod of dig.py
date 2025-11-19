import yogi

n = yogi.scan(int)
copyn = n
while n is not None:
    if n %10 == n:
        print ("The product of the digits of", n , "is" , n , end = '')
        print (".")
    else:
        prod = 1
        while (n // 10) != 0:
            copyn = n
            prod = 1
            while n//10 > 0:
                prod = prod * (n%10)
                n = n//10
            prod = prod * (n%10)
            n = prod
            print ("The product of the digits of", copyn , "is" , prod , end = '')
            print (".")
    print ("----------")
    n = yogi.scan(int)

import yogi
if __name__ == "__main__":
    n = yogi.read(int)
    x = n
    i = 1
    while x//10 != 0:
        x = x//10
        i = i + 1
    print ("The number of digits of" , n , "is" , i)

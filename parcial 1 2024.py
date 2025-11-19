import yogi
def surprise(n):
    r = 0
    while n != 0:
        d = n%10
        r = (r*10+(d+1)%10)*10+d
        n = n//10
    return r

def reverse(n):
    r = 0
    while n != 0:
        r = r*10 + n%10
        n = n // 10
    return r
def meitatsCapicues(n):
    a = 0
    b = 0
    for i in range (4):
        a = a + ((n%10)*(10**i))
        n = n // 10
    for i in range (4):
        b = b + ((n%10)*(10**i))
        n = n // 10
    return (a == reverse(a) and b == reverse(b))

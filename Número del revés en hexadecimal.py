import yogi
n = yogi.read(int)
r = 0
while n//16 != 0:
    r = n%16
    if r == 10:
        r = "A"
    elif r == 11:
        r = "B"
    elif r == 12:
        r = "C"
    elif r == 13:
        r = "D"
    elif r == 14:
        r = "E"
    elif r == 15:
        r = "F"
    print (r, end = '')
    n = n//16
r = n%16
if r == 10:
    r = "A"
elif r == 11:
    r = "B"
elif r == 12:
    r = "C"
elif r == 13:
    r = "D"
elif r == 14:
    r = "E"
elif r == 15:
    r = "F"
print (r)

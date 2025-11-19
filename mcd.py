import yogi
a = yogi.read(int)
b = yogi.read(int)
mcd = a
div = b
while div != 0:
    mcd, div = div, mcd%div
print ("The gcd of" , a , "and" , b , "is", mcd, end = '')
print (".")

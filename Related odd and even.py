import yogi
n = yogi.read(int)
copyn = n
ndig = 0
parell = 0
senar = 0
while n > 0:
    parell = parell + (n%10)
    n = n//10
    n = n//10
while copyn > 0:
    copyn = copyn//10
    senar = senar + (copyn%10)
    copyn = copyn//10
print (parell , senar)
a = parell
b = senar
if a != 0 and b % a == 0:
    print (b , "=" , (b//a), "*" , a)
elif b != 0 and a % b == 0:
    print (a , "=" , (a//b), "*" , b)
else:
    print ("nothing")

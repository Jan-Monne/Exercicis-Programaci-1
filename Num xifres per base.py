import yogi
n = yogi.read(int)
ndig = 1
r = n
for i in range(2,17):
    ndig = 1
    r = n
    while r//i != 0:
        r = r//i
        ndig = ndig + 1
    print ("Base" , i , end = '')
    print (":" , ndig , "cifras.")

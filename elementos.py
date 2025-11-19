import yogi
u = yogi.read(str) #u porque es el Uno
d = yogi.read(str) #d porque es el Dos
r = 0 #r porque es el Resultado
if (u == "V" and d == "A"):
    r = "1"
elif (u == "A" and d == "V"):
    r = "2"
elif (u < d):
    r = "1"
elif (u > d):
    r = "2"
elif (u == d):
    r = "-"
print (r)

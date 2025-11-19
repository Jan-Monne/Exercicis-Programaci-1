import yogi
print ("Quantes hores vols sumar?")
nhores = yogi.read(int)
suma = 0
for i in range (nhores):
    h = yogi.read(int)
    m = yogi.read(int)
    s = yogi.read(int)
    suma = suma + (h*3600 + m*60 + s)
print (suma)

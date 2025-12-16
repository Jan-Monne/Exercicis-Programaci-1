import yogi
with open("datos.txt","r") as f:
    senars = int(f.readline())
    parells = int(f.readline())
    pos = 1
    for linea in f:
        x = int(linea.strip())
        if pos % 2 == 0:
            if x < parells:
                parells = x
        else:
            if x > senars:
                senars = x
        pos += 1
print ("El maxim dels valors en posicions senars es:", senars)
print ("El minim dels valors en posicions parells es:", parells)
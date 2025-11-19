import yogi
print ("A quina hora vols que li afegeixi un segon?")
hores = yogi.read(int)
minuts = yogi.read(int)
segons = yogi.read(int)
segons = segons + 1
if (segons == 60):
    segons = "00"
    minuts = minuts + 1
elif (segons < 10):
    segons = str(segons)
    segons = "0" + segons
if (minuts == 60):
    minuts = "00"
    hores = hores + 1
elif (minuts < 10):
    minuts = str(minuts)
    minuts = "0" + minuts
if (hores == 24):
    hores = "00"
elif (segons < 10):
    hores = str(hores)
    hores = "0" + hores
print(hores, ":" , minuts , ":" , segons)
print ("Aquest es el teu nou temps!")

import yogi
lletra = yogi.read(str)
mayus = "QWERTYUIOPASDFGHJKLÑÇZXCVBNM"
vocals = "AaEeIiOoUu"
if (lletra in mayus):
    print ("majuscula")
else:
    print ("minuscula")
if (lletra in vocals):
    print ("vocal")
else:
    print ("consonant")

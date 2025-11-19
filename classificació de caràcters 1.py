import yogi
a = yogi.read(str)
if ((a <= "Z" and a >= "A") or a == "Ç" or a == "Ñ"):
    print ("Majuscula")
else:
    print ("Minuscula")
if (a == "A" or a == "a" or a == "E" or a == "e" or a == "I" or a == "i" or a == "O" or a == "o" or a == "U" or a == "u"):
    print ("Vocal")
else:
    print ("Consonant")

def fatten(n):
    copyn = n
    flipn = "0"
    while n // 10 != 0:
        flipn = flipn + str(n % 10)
        n = n //10
    flipn = flipn + str(n % 10)
    return int(flipn)
#no acabat i no funciona per a 1200 o 900 ja que flipn = 21 o 9

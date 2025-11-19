# Feu un programa que, donada una quantitat de segons, digui quantes hores,
# minuts i segons representa
# Escriviu tres naturals h, m, s tals que 3600h +60m +s = n, amb m < 60 i s < 60.
import yogi
n = yogi.read(int)
h = n // 3600
m = (n % 3600) // 60
s = (n % 3600) % 60
print (h, m, s)

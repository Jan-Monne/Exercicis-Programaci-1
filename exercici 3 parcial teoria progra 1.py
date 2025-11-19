import yogi
def sumaXifres(n):
    mil = (n // 1000) % 10
    cent = (n // 100) % 10
    des = (n // 10) % 10        

    return mil + cent + des
a = yogi.read(int)
suma = 0
for i in range(a):
    n = yogi.read(int)
    n = sumaXifres(n)
    suma = suma + n
print (suma/a)

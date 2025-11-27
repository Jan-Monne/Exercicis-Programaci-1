import yogi
n = yogi.scan(int)
while n is not None:
    equal = False
    suma = 0
    llista = []
    for i in range (n):
        x = yogi.read(int)
        llista.append(x)
    for x in llista:
        suma += x
    for x in llista:
        if x == suma-x:
            equal = True
            break
    if equal:
        print("YES")
    else:
        print("NO")
    n = yogi.scan(int)
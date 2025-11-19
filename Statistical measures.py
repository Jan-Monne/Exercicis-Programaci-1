import yogi
n = yogi.read(int)
for i in range (n):
    e = yogi.read(int)
    suma = yogi.read(float)
    max = suma
    min = suma
    for j in range (e-1):
        x = yogi.read(float)
        suma += x
        if max < x:
            max = x
        if min > x:
            min = x
    print(f"{min:.4f}", f"{max:.4f}", f"{suma/e:.4f}")

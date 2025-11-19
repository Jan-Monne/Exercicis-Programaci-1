import yogi
x = yogi.scan(float)
suma = 0.0
n = 0.0
while x is not None:
    suma += x
    n += 1.0
    x = yogi.scan(float)
print(f"{suma / n:.2f}")

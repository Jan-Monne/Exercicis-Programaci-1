import yogi
x = yogi.read(float)
c = yogi.scan(float)
e = 0
total = 0.0
while c is not None:
    total += c*(x**e)
    e += 1
    c = yogi.scan(float)
print(f"{total:.4f}")

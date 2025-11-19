import yogi
x = yogi.read(float)
c = yogi.scan(float)
total = 0.0
while c is not None:
    total = (x*total)+c
    c = yogi.scan(float)
print(f"{total:.4f}")
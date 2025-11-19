import yogi
h = yogi.read(int)
m = yogi.read(int)
s = yogi.read(int)
suma = 0
hstart = h
while h == hstart:
    s = s + 1
    suma = suma + 1
    if s == 60:
        s = 0
        m = m + 1
        if m == 60:
            m = 0
            h = h + 1
            if h == 24:
                h = 0
print ("Nova hora h=" + str(h) + " m =" + str(m) + " s=" + str(s))
print ("Segons sumats" , suma)

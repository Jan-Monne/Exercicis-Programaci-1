#L’entrada consisteix en tres naturals h, m i s que representen una hora del dia,
#es a dir, tals que h < 24, m < 60 i s < 60.
import yogi
h = yogi.read(int)
m = yogi.read(int)
s = yogi.read(int)
s = s + 1
if (s == 60):
    s = 0
    m = m + 1
    if (m == 60):
        m = 0
        h = h + 1
        if (h == 24):
            h = 0
if (s < 10):
    s = "0" + str(s)
if (m < 10):
    m = "0" + str(m)
if (h < 10):
    h = "0" + str(h)
print (h ,  ":" , m , ":" , s, sep='')

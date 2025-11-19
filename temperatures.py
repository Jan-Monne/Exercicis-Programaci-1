import yogi
t = yogi.read(int)
if t >= 10 and t <=30:
    print ("s'esta be")
elif t < 10:
    print ("fa fred")
    if t <= 0:
        print ("l'aigua es gelaria")
elif t > 30:
    print ("fa calor")
    if t >= 100:
        print ("l'aigua bulliria")

import yogi
p = yogi.read(str)
first = p[0]
last = p[-1]
if first == ")" or last == "(":
    print ("no")
else:
    opened = 0
    closed = 0
    for parentesis in p:
        if parentesis == "(":
            opened += 1
        else:
            closed += 1
    if closed == opened:
        print ("yes")
    else:
        print ("no")
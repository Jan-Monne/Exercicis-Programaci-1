import yogi
p = yogi.scan(str)
if p is None:
    print("yes")
else:
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
            if opened < closed:
                break
        if closed == opened:
            print ("yes")
        else:
            print ("no")
def vectorEnOrdreEnter():
    positius = []
    negatius = []
    with open("datos.txt","r") as f:
        for line in f:
            x = int(line.strip())
            if x < 0:
                negatius.append(x)
            else:
                positius.append(x)
    negatius.reverse()
    total = negatius + positius
    return total
def sameButEfficient():
    v = []
    with open("datos.txt","r") as f:
        for line in f:
            x = int(line.strip())
            if x < 0:
                v.insert(0,x)
            else:
                v.append(x)
    return v
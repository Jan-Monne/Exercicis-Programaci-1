def tri_creixent(v):
    l = len(v)
    vec = []
    for i in range (l, 3):
        num = 100*v[i] + 10*v[i+1] + v[i+2]
        vec.append(num)
    for i in range (0, l-1):
        if v[i] > v[i+1]:
            return False
    return True 
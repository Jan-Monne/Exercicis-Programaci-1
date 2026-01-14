def majorAnteriors(v):
    if len(v) <= 1:
        return False
    for i in range (1, len(v)):
        if v[i] > v[0]:
            return True
    return False

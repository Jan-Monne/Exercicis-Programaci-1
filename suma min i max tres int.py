import yogi
def sum_min_max(a, b, c):
    min = 0
    max = 0
    if (a<b and a<c):
        min = a
    elif (b<a and b<c):
        min = b
    elif (c<a and c<b):
        min = c
    if (a>b and a>c):
        max = a
    elif (b>a and b>c):
        max = b
    elif (c>a and c>b):
        max = c
    return (min + max)

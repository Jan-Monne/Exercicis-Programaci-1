def sum_min_max(x, y, z):
    if x <= y and x <= z:
        minim = x
    elif y <= x and y <= z:
        minim = y
    elif z <= x and z <= y:
        minim = z
    if x >= z and x >= y:
        maxim = x
    elif y >= z and y >= x:
        maxim = y
    elif z >= x and z >= y:
        maxim = z
    return (minim + maxim)

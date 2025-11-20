def fatten(n):
    n = str(n)
    prev = 0
    num = ''
    for c in n:
        digit = int(c)
        if digit < prev:
            num += str(prev)
        else:
            num += c
            prev = digit
    return num

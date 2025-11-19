import yogi
def number_of_digits(n):
    ndig = 1
    while n//10 != 0:
        n = n //10
        ndig = ndig+1
    return ndig

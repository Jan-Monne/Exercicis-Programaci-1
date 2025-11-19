import yogi
import math
def is_perfect(n):
    if n == 0:
        return False
    else:
        suma = 0
        copyn = n
        arrel = int(math.sqrt(n))
        for i in range (1, arrel+1):
            if n % i == 0:
                suma += i
                if i != n//i:
                    suma += n//i
        suma -= copyn
        if suma == copyn:
            return True
        else:
            return False

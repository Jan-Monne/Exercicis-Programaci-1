import yogi
import math
def sum_divisors(n):
    suma = 0
    if n == 0:
        suma = 0
    arrel = int(math.sqrt(n))
    for i in range (1, arrel + 1):
        if n % i == 0:
            suma = suma + i
            if i != x//i:
                suma = suma + (n//i)
    return suma
                

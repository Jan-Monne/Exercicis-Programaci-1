import math

#Llegir els coeficients
a = float(input('a= '))
b = float(input('b= '))
c = float(input('c= '))

#Calcular el discriminant
d = b**2 - 4*a*c

#Calcular les arrels
if (a!=0 and d>0):
    x1 = (-b + math.sqrt(d)) / (2*a)
    x2 = (-b - math.sqrt(d)) / (2*a)
    print (x1,x2)
else:
    print ("No es pot calcular")


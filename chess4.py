import yogi
n = yogi.read(int)
blancas = 0
negras = 0
for i in range(1, n + 1):
    line = input()                          #lee línea x línea
    casilla_blanca = (i % 2 != 0)           #inicializa una variable booleana para controlar el acceso a casillas blancas
    for c in line:                          #accede caracter x caracter en cada línea
        if casilla_blanca:
            blancas += ord(c) - ord('0')    #ord(character) es el código ASCII del caracter
        else:
            negras += ord(c) - ord('0')
        casilla_blanca = not casilla_blanca #va alternando casilla blanca-casilla negra
print(blancas,'-',negras,sep='',end='')     #hay que adecuar el formato de salida a la especificación
print(' = ',blancas - negras)

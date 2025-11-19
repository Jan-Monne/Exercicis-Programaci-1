import yogi
n = yogi.read(int)
matriu = 1
for i in range (n-1):
    matriu += 2
files = matriu-1
columnes = matriu
asteriscs = 1
for i in range ((columnes//2)+1):
    for j in range (files//2):
        print(" ", end = '')
    for j in range (asteriscs):
        print ("*", end = '')
    print()
    asteriscs += 2
    files -= 2
asteriscs -= 2
files += 2
for i in range (columnes//2):
    asteriscs -= 2
    files += 2
    for j in range (files//2):
        print(" ", end = '')
    for j in range (asteriscs):
        print ("*", end = '')
    print()

import yogi
x = yogi.read(int)
sub = 1
pre = x
while x != -1:
    if x != pre:
        sub += 1
    pre = x
    x = yogi.read(int)
print ("Hi ha", sub , "subseqüències amb el mateix valor repetit")

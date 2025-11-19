import yogi
print ("Quin import vols extreure d'aquest caixer?")
a = yogi.read(int)
print ("Et donarem aquests bitllets/monedes:")
if (a//100 != 0):
    print (a//100 , " bitllet de 100€")
    a = a- (a//100)*100
if (a//50 != 0):
    print (a//50 , " bitllet de 50€")
    a = a- (a//50)*50
if (a//20 != 0):
    print (a//20 , " bitllet de 20€")
    a = a- (a//20)*20
if (a//10 != 0):
    print (a//10 , " bitllet de 10€")
    a = a- (a//10)*10
if (a//5 != 0):
    print (a//5 , " bitllet de 5€")
    a = a- (a//5)*5
if (a//2 != 0):
    print (a//2 , " moneda de 2€")
    a = a- (a//2)*2
if (a//1 != 0):
    print (a//1 , " moneda de 1€")
    a = a- (a//1)*1
print ("Gràcies per venir a aquest caixer :)")

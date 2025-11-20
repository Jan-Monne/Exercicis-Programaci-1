import yogi
word = yogi.scan(str)
firstmax = "" #This variable stores the largest word in alphabetical order.
secondmax = "" #This variable stores the 2nd largest word in alphabetical order.
while word is not None:
    if word > firstmax:
        secmax = firstmax 
        firstmax = word
    elif word < firstmax and word > secmax:
        secmax = word
    word = yogi.scan(str)
print (secmax)
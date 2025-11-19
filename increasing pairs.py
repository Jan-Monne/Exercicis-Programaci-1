import yogi
n = yogi.read(int)
for i in range(n):
    count = 0
    pre = yogi.read(int)
    if pre != 0:
        act = yogi.read(int)
        while act != 0: 
            if pre < act:
                count += 1
            pre = act
            act = yogi.read(int)
    print (count)
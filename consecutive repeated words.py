import yogi
og = yogi.scan(str)
sub = 0
highest = 0
if og is not None:
    act = og
    while act is not None:
        if act == og:
            sub += 1
            if sub > highest:
                highest = sub
        else:
            sub = 0
        act = yogi.scan(str)
print(highest)
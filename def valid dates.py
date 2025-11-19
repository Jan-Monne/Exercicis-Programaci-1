import yogi
def is_valid_date(d, m, y):
    if (d>0 and d<32 and m>0 and m<13):
        if m==2:
            if y%4 == 0 and d<30:
                if y%100 != 0:
                    return True
                else:
                    if (y//100)%4 == 0:
                        return True
                    elif ((y//100)%4 != 0) and d<29:
                        return True
                    else:
                        return False
            else:
                if d<29:
                    return True
                else:
                    return False
                
        elif m==4 or m==6 or m==9 or m==11:
            if d<31:
                return True
            else:
                return False
        else:
            return True
    else:
        return False







#mesos 31: 1, 3, 5, 7, 8, 10, 12
#mesos 30: 4, 6, 9, 11
#mes 28 o 29 en leap: 2

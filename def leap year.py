def is_leap_year(n):
    if n % 4 == 0:
        if n % 10 == 0:
            n = n // 10
            if n % 10 == 0:
                n = n //10
                if n % 4 == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return True
    else: return False

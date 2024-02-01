from math import sqrt

def threesquares(m):
    res = False
    
    if m<0:
        return res
    
    sum = 0
    limit = int(sqrt(m))+1
    
    while sum <= m:
        for x in range(0, limit):
            for y in range(0, limit):
                for z in range(0, limit):
                        sum = x**2 + y**2 + z**2
                        if sum == m:
                            res = True
                            return res
                        elif sum>m:
                            break
    return res
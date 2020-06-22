def logical_and(stands):
    n = len(stands)
    i = 1
    x = stands[0]
    while i < n:
         x = x & stands[i]
         i +=1
    return bool(x)


def logical_or(stands):
    n = len(stands)
    i = 1
    x = stands[0]
    while i < n:
         x = x | stands[i]
         i +=1
    return bool(x)


def logical_xor(stands):
    n = len(stands)
    i = 1
    x = stands[0]
    T = 0
    if bool(x):
        T=1
    while i < n:
         if bool(stands[i]):
             T +=1
         x = x | stands[i]
         i +=1
    if T<2:
        return bool(x)
    else:
        return bool(0)



def logical_nor(*input):
    n = len(stands)
    i = 1
    x = stands[0]
    while i < n:
         x = x | stands[i]
         i +=1
    return not bool(x)


def logical_nand(*input):
    n = len(stands)
    i = 1
    x = stands[0]
    while i < n:
         x = x & stands[i]
         i +=1
    return not bool(x)


stands = (1,1,1,1,1,1,1,1,1,1)
print(logical_nand(stands))





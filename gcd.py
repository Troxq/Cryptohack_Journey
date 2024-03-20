def gcd(r2, r1):
    if(r2%r1 == 0):
        return r1
    return gcd(r1, r2%r1)

print(gcd(66528, 52920))


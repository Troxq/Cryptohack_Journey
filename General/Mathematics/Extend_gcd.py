def Egcd(a, b):
    if (b==0):
        return 1, 0, a
    x2, y2, gcd = Egcd(b, a%b)
    x = y2
    y = x2 - (a//b) * y2
    return x, y, gcd

u, v, gcd = Egcd(3, 13)
print(u, v, gcd)
print((u * 26513) + (v * 32321))
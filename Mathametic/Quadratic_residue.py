def qr(mod):
    x = []
    for i in range(1, mod):
        c1 = pow(i, 2) % mod
        #c2 = pow((mod-i), 2) % mod
        x.append(c1)
        #x.append(c2)
    return x    

print(qr(29))
from Crypto.PublicKey import RSA

with open("Cryptohack_Journey/General/DataFormat/bruce_rsa.pub", "rb") as f:
    data = f.read()
    key = RSA.importKey(data)
    print(key.n)
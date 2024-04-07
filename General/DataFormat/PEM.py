from Crypto.PublicKey import RSA

with open("General/DataFormat/RSA.pem", "rb") as f:
    data = f.read()
    key = RSA.import_key(data)
    print(key.d)


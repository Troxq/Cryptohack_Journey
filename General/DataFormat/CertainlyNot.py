from Crypto.PublicKey import RSA

#openssl x509 -inform DER -in cert.der -outform PEM -out cert.pem

with open("General/DataFormat/cert.pem", "r") as pem:
    pemfile = pem.read()

rsa = RSA.import_key(pemfile)

print(rsa.n)


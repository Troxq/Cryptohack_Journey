from pwn import *
from Crypto.Util.number import *

problem = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"

prob_bytes = bytes.fromhex(problem)

f = "crypto{" #First 7 bytes
f_bytes = f.encode()

key = xor(f_bytes, prob_bytes[0:7])
print(key)
key += b'y'

flag = xor(key, prob_bytes)
print(flag.decode())


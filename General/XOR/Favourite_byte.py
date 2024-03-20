from Crypto.Util.number import *
from pwn import *

problem = 0x73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d

for i in range(0, 128): #All ASCII range
    print(long_to_bytes(i ^ problem))
          
problem = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"

for i in range(0, 128): #All ASCII range
    x = xor(i, bytes.fromhex(problem))
    if ("b'crypto{" in str(x)): print(x)

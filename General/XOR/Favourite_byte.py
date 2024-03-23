from Crypto.Util.number import *
from pwn import *

problem = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"

for i in range(0, 128): #All ASCII range
    x = "".join([chr(i ^ x) for x in bytes.fromhex(problem)])
    if ("crypto" in x):
        print(x)
          
# problem = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"

# for i in range(0, 128): #All ASCII range
#     x = xor(i, bytes.fromhex(problem))
#     #if ("b'crypto{" in str(x)): print(x)

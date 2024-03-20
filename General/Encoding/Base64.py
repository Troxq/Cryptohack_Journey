import base64

problem = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

bytestr = bytes.fromhex(problem)

base64 = base64.b64encode(bytestr)

print(base64)
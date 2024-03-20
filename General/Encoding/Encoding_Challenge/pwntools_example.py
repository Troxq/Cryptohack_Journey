from pwn import * # pip install pwntools
import base64
import json
import codecs
from Crypto.Util.number import bytes_to_long, long_to_bytes

r = remote('socket.cryptohack.org', 13377, level = 'debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

#print("Received type: ")
#print(received["type"])
#print("Received encoded value: ")
#print(received["encoded"])

for x in range(0, 100):
    received = json_recv()
    Type = received["type"]
    Encode = received["encoded"]

    if (Type == "base64"):
        Decode = base64.b64decode(Encode).decode()
    elif (Type == "hex"):
        Decode = bytes.fromhex(Encode).decode()
    elif (Type == "rot13"):
        Decode = codecs.decode(Encode, "rot13")
    elif (Type == "bigint"):
        Decode = long_to_bytes(int(Encode, 0)).decode()
    elif (Type == "utf-8"):
        Decode = "".join([chr(x) for x in Encode])

    to_send = {
        "decoded": Decode
    }
    json_send(to_send)
print(json_recv()["flag"])
hex_string = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
integer = 1

# XOR directly with the string
result_string = ''.join(chr(int(c, 16) ^ integer) for c in hex_string)

# Convert the string to bytes first
hex_bytes = bytes.fromhex(hex_string)
result_bytes = bytes([b ^ integer for b in hex_bytes])

print("XOR result using string:", result_string)
print("XOR result using bytes:", result_bytes.hex())
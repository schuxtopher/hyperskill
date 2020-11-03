message = input()
key = sum(int(input()).to_bytes(2, 'little'))

print(''.join([chr(ord(x) + key) for x in message]))

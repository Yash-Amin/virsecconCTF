from base64 import b64decode as decode

with open('urldecoded', 'r') as f:
    urlencoded = f.read().strip()
    decoded = decode(urlencoded)

with open('b64decode', 'wb') as f:
    f.write(decoded)

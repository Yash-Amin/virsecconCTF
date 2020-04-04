from urllib.parse import unquote

with open('js_out', 'r') as f:
    urlencoded = f.read().strip()
    decoded = unquote(urlencoded)
with open('urldecoded', 'w') as f:
    f.write(decoded)

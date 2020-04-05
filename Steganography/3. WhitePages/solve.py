from urllib.parse import quote

with open('whitepages.txt', 'rb') as f:
    data = f .read()
    # print(quote(data))
    data = quote(data)
    out = data.replace('%', '')
    out = out.replace('E28083', '0')
    out = out.replace('20', '1')

    # print(out)
    try:
      for i in range(1000):
        print(chr(int(out[i * 8: (i+1) * 8], 2)), end='')
    except:
      pass
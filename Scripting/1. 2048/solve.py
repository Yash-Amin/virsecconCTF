from base64 import b64encode as encode
from base64 import b64decode as decode


    # i = 2
for i in range(3,100):
    inp = '2048' + '_' + str(i-1)
    op = '2048' + '_' + str(i)

    with open(inp, 'r') as f:
        x = f.read().splitlines()
        text = ''
        for z in x:
            text += z
        text = text.replace(' ','')
        text = text.replace('\r','')
        text = text.replace('\n','')


    d = decode(text.encode()).decode('utf8')
    with open(op, 'w') as f:
        f.write(d)


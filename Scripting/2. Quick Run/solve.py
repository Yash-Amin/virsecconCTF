

# pip install pyqrcode

from pyzbar.pyzbar import decode
from PIL import Image


for i in range(1, 31):
    x = decode(Image.open(str(i) + '.png'))[0]
    data = x.data.decode('utf8')
    print(chr(int(data)), end='')
print()
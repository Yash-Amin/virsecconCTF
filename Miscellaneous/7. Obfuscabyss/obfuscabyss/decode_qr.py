


# pip install pyqrcode

from pyzbar.pyzbar import decode
from PIL import Image


x = decode(Image.open('image.png'))[0]
data = x.data#.decode('utf8')
with open('decoded_qr.txt', 'wb') as f:
    f.write(data)
print(data)
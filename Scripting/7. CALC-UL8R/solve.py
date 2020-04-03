''' 
    Solution:
    Flag:  LLS{sympy_to_solve_equations}
'''

# nc jh2i.com 50003
from pwn import *
from sympy import * 
conn = remote('jh2i.com',50003)

for i in range(7):
    print(conn.recvline(timeout=1))

print('----')
while True:
    eq = conn.recvline().decode()
    if eq.strip() == '':
        print('zzz')
        continue
    print('>>', eq)
    if '{' in eq:
        break
    sympy_eq = sympify("Eq(" + eq.replace("=", ",") + ")")
    ans = str(solve(sympy_eq)[0]).encode() 
    print('ans', '=', ans)
    conn.send(ans)
    conn.recvline().decode()

for i in range(4):
    print('!', conn.recvline(timeout=1))
conn.close()



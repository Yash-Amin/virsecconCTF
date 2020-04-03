one = 'encrypted_one.png'
two = 'encrypted_two.png'


from PIL import Image
i1 = Image.open(one) 
i2 = Image.open(two) 
m1 = i1.load()
m2 = i2.load()
print (i1.size) 
print (i2.size) 

x,y = i1.size

R,G,B,A = open('R', 'wb'),open('G', 'wb'),open('B', 'wb'),open('A', 'wb')

for i in range(x):
    for j in range(y):
        r1,g1,b1,a1 = m1[i,j]
        r2,g2,b2,a2 = m2[i,j]

        R.write(chr(r1 ^ r2).encode())
        G.write(chr(g1 ^ g2).encode())
        B.write(chr(b1 ^ b2).encode())

        A.write(chr(r1 ^ r2^ g1 ^ g2^ b1 ^ b2).encode())
    # print (pix[0,0]) 



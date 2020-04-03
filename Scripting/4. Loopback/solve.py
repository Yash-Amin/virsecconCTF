 
from pcapfile import savefile
testcap = open('loopback.pcap', 'rb')
capfile = savefile.load_savefile(testcap,layers=3, verbose=True)
z = 0
with open('hex', 'w') as f:
    for i in range(len(capfile.packets)):
        pkt = capfile.packets[i]
        x = pkt.packet.payload.payload.decode('utf8')

        if '7b' in x and '7d' in x:
            if x.index('7b') < x.index('7d'):
                try:
                    # bytearray.fromhex(x).decode()
                    f.write(x + '\n')
                    print(x)
                    z += 1
                except:
                    pass


print(z)
from socket import *
s=socket()
s.connect(("127.0.0.1",345))
s.send(("connection established").encode())
fp=open("678.png","ab")
frec=s.recv(1024)
while(frec):
    fp.write(frec)
    frec=s.recv(1024) 
    
fp.close()
s.close()

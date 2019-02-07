from socket import *
s=socket(AF_INET,SOCK_STREAM)
s.bind(('',345))
s.listen(3);
soc,sadd=s.accept()
fp=open("123.png","rb")
fpart=fp.read(1024)
while(fpart):
    soc.send(fpart)
    fpart=fp.read(1024)
fp.close()
s.close()

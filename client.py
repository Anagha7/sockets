from socket import *
from threading import Thread
import sys

def receive():
    #This fn is for the client to receive msgs from the server
    while True:
        rmsg=s.recv(1024).decode()
        print(rmsg+"\n")
def send():
    #This fn is to take user input from the keyboard and send to the server
    while(True):
        smsg=input("->")
        if smsg=="exit":
            s.close()
            break
        else:
             s.send(smsg.encode())
        
    
    
server_ip=sys.argv[1]
server_port=int(sys.argv[2])
s=socket(AF_INET,SOCK_STREAM)
s.connect((server_ip,server_port))
tr=Thread(target=receive)
ts=Thread(target=send)
tr.start()
ts.start()


from socket import *
from threading import Thread 





def accept_connect() :
   
   while(True):
        #print("hello listening.."); 
        csoc,cadd=s.accept()
        Client_add[csoc]=cadd
        print(str(cadd) +"is connected")
        msg="Welcome  "+str(cadd)+"Enter your name and press enter\n"
        csoc.send(msg.encode())
        name=csoc.recv(size).decode()
        csoc.send(("Welcome "+name+"To exit the chat please enter {exit}\n").encode())
        Clients[csoc]=name
        th2=Thread(target=chat,args=(csoc,Clients)).start()

def chat(csoc,Clients):
    msg=(csoc.recv(size)).decode()
    if(msg=="exit"):
       
        csoc.send((name+"is leaving the chat\n").encode())
        csoc.close()
        del Clients[csoc]
    else:
        for client in Clients:
            print("message")
            csoc.send(msg.encode())
                      
                  
              
        
       
        
    
Clients={}
Client_add={}
ip=''
port=333
size=2028
s=socket(AF_INET,SOCK_STREAM)
s.bind((ip,port))
s.listen(5)
Th=Thread(target=accept_connect)

Th.start()
Th.join()


    

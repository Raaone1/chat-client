import socket
import select
import sys
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(),10010))
input1=[s]
run=1
s.listen(5)
adr=[]
while run:
    inputr,output,exc=select.select(input1,[],[])
    for x in range(len(inputr)):
        if inputr[x]==s:
            s1,addr=s.accept()
            print("Got connection from "+str(addr))
            input1.append(s1)
            adr.append(addr)            
        else:
            c2=inputr[x].recv(1000)
            print("Got message from "+str(adr[x-1]))                    
            stri=c2.decode()
            if stri=='exit':
                input1.pop([x])
                for y in range(1,len(input1)):
                    if input1[y]!=inputr[x]:
                        input1[y].send(('Client at %s has been removed from the chat'%(str(adr[x-1])).encode())
                adr.pop([x-1])
            else:
                for y in range(1,len(input1)):
                    if input1[y]!=inputr[x]:
                        input1[y].send(("Client at %s writes: %s"%(str(adr[x-1]),stri)).encode())
    if len(input1)==1:
        run=0	  	
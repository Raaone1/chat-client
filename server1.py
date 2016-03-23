import socket
import select
import sys
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(),10010))
input1=[s,sys.stdin]
running=1
s.listen(1)
while running:
	inputr,output,exc=select.select(input1,[],[])
    for x in inputr:
    	if x==s:
	        s1,addr=s.accept()
            print("Client is at "+str(addr))
            input1.append(s1)
        elif x==sys.stdin:
            c1=sys.stdin.readline()
            if c1=='exit':
                running=0
            else:
                s1.send(c1.encode())            
        else:
            c2=x.recv(1000)
            print(c2.decode())
s1.close()	  	
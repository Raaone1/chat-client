import socket
import sys
import select
s1=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s1.connect((socket.gethostname(),10030))
print("Got connected to "+socket.gethostname())
input1=[s1,sys.stdin]
running=1
while running:
    input2,out,exc=select.select(input1,[],[])
    for x in input2:
        if x==s1:
            c1=s1.recv(1000)
            print(c1.decode())
        elif x==sys.stdin:
            c2=sys.stdin.readline()
            s1.send(c2.encode())
            if c2=='exit':
                running=0
s1.close()    
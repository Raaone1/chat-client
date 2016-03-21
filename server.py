import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(),10010))
s.listen(1)
s1,addr=s.accept()
c1="Client is at "+str(addr)
print(c1)
while 1:
    c2=s1.recv(1000)
    print(c2.decode())
    c3=input(">")
    s1.send(c3.encode())
s1.close()
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((socket.gethostname(),10010))
c1="Got connected to "+socket.gethostname()
print(c1)
while 1:
    c2=input("Enter some shit:")
    s.send(c2.encode())
    c3=s.recv(1000)
    print(c3.decode())
s.close()    
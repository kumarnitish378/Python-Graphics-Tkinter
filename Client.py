import socket
import os
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
print(s)
host = socket.gethostbyname("127.0.0.1")
s.connect((host,5000))
s.send(b"hello this is client2 ")
print(s.recv(1024))
while True:
    #s.send(b"hello this is client2 ")
    print(s.recv(1024))
    data = "nitish 2 =>> "+input("nitish2-->> ")
    s.send(bytes(data,encoding='utf-8'))
    print("_____________________________________")
    #print(s.recv(1024))
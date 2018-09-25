__author__ = 'DELL'
#CLIENT SIDE
import socket
host ="localhost"
port = 12345
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))
sk = input("Enter data")
while sk != 'exit':
    s.send(sk.encode())
    data = s.recv(1024)
    data = data.decode()
    print("from receiver "+data)
    sk = input("Enter data")
s.close()

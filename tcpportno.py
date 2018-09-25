__author__ = 'DELL'
import socket
host = "localhost"
ip = socket.gethostbyname(host)
print("scanning port :",ip)
print("Port hosting the tcp server is:")
for port in range(1,1024):
    s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    c=s.connect_ex((host,port))
    if c == 0:
        print("OPEN PORT: ",port)
        break
    s.close()


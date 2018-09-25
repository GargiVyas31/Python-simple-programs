__author__ = 'DELL'
import socket
s = socket.socket()
host = "localhost"
port = 60000
s.connect((host,port))
s.send(bytes(("Hello Server").encode()))
with open('receivedfile.txt', 'wb') as f:
    print("file opened")
    while True:
        print("Receinving data")
        data = s.recv(1024)
        print("data =  ",(data))
        if not data:
            break
    f.write(data)
f.close()
print("Succesfully got the file")
s.close()
print("socket connection closed")

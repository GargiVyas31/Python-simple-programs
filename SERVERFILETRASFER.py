__author__ = 'DELL'
import socket
port = 60000
host = "localhost"
s = socket.socket()
s.bind((host,port))
s.listen(1)
print("Server is listening")
while True:
    c , add = s.accept()
    print("Got connection from ",add)
    data = c.recv(1024)
    print("Server received",repr(data))
    filename= "mytext.txt"
    f = open(filename,'rb')
    l= f.read(1024)
    while (l):
        c.send(l)
        print("sent ",repr(l))
        l=f.read(1024)
    f.close()
    print("Done sending")
    c.send(bytes(("Thankyou for connecting").encode()))
    c.close()



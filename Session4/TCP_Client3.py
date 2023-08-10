import socket
import random
import time

host = '192.168.1.15'
port = 2001

ClientSocket = socket.socket()
print('Waiting for connection')

ClientSocket.connect((host, port))

Response = ClientSocket.recv(2048)
time.sleep(1)

while True:
    message = "Control signal is "+ "on" if(str(random.random()<0.5))else('off')
    ClientSocket.send(str.encode(message))
    time.sleep(3)

ClientSocket.close()

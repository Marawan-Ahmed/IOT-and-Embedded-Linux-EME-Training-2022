import socket
from _thread import *
import time

comm_channel =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_ip ="192.168.1.15"
host_port = 2001
comm_channel.bind((host_ip,host_port))

comm_channel.listen()

def client_handler(connection,id):
    connection.send(str.encode('You are now connected to the replay server... Type BYE to stop'))
    while True:
        time.sleep(1)
        data = connection.recv(2048)
        message = data.decode('utf-8')
        print("Message from client "+ str(id) + " is " + message)
        if message == 'BYE':
            break
    connection.close()


while 1:
    Client, address = comm_channel.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(client_handler, (Client, address))

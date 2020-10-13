from flask import Flask
import os
import threading
import socket


class SocketWrapper:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __del__(self):
        self.sock.close()


app = Flask(__name__)
app.config['LAST_PHOTO'] = "no_data"


def server_socket():
    serversocket = SocketWrapper()
    serversocket.sock.bind((socket.gethostname(), 1236))
    serversocket.sock.listen(5)

    print("Created socket")

    while True:
        (clientsocket, address) = serversocket.sock.accept()

        x = clientsocket.recv(1000)
        app.config['LAST_PHOTO'] = x.decode('ascii')
        clientsocket.close()


x = threading.Thread(target=server_socket)
x.start()


from app import routes

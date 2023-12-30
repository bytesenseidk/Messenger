import os
import socket

class ServerHandler(object):
    def __init__(self, IP="127.0.0.1", PORT=1234):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((IP, PORT))
        self.server_socket.listen()
        self.HEADER_LENGTH = 10
        self.sockets_list = [self.server_socket]
        self.clients = {}
        os.system("cls")
        print(f"[ SERVER UP AND RUNNING ]\n[IP: {IP}]\n[Port: {PORT}]\n")

    def receive_message(self, client_socket):
        try:
            message_header = client_socket.recv(self.HEADER_LENGTH)
            if not len(message_header):
                return False
            message_length = int(message_header.decode("utf-8").strip())
            return {"header": message_header, "data": client_socket.recv(message_length)}
        except:
            return False

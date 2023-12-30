import socket

class ClientHandler(object):
    def __init__(self, my_username, IP="127.0.0.1", PORT=1234):
        self.my_username = my_username
        self.HEADER_LENGTH = 10

        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((IP, PORT))
        self.client_socket.setblocking(False)

        username = my_username.encode('utf-8')
        username_header = f"{len(username):<{self.HEADER_LENGTH}}".encode('utf-8')
        self.client_socket.send(username_header + username)

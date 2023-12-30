import sys
import errno
from client_handler import ClientHandler

class Client(object):
    def __init__(self, username, ip, port):
        self.client = ClientHandler(username, ip, port)
    
    def run(self):
        while True:
            message = input(f"{self.client.my_username}  >> ")
            if message:
                message = message.encode('utf-8')
                message_header = f"{len(message):<{self.client.HEADER_LENGTH}}".encode('utf-8')
                self.client.client_socket.send(message_header + message)
            try:
                while True:
                    username_header = self.client.client_socket.recv(self.client.HEADER_LENGTH)
                    if not len(username_header):
                        print("\nConnection terminated by the server!")
                        sys.exit()
                    username_length = int(username_header.decode('utf-8').strip())
                    username = self.client.client_socket.recv(username_length).decode('utf-8')
                    message_header = self.client.client_socket.recv(self.client.HEADER_LENGTH)
                    message_length = int(message_header.decode('utf-8').strip())
                    message = self.client.client_socket.recv(message_length).decode('utf-8')
                    print(f'{username}  >> {message}')
            except IOError as e:
                if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
                    print(f'Reading error: {str(e)}')
                    sys.exit()
                continue
            except Exception as e:
                print(f'Reading error: {str(e)}')
                sys.exit()

if __name__ == "__main__":
    Client("bytesensei", "127.0.0.1", 1234).run()
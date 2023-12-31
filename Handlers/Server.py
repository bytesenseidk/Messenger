import sys
import select
from server_handler import ServerHandler
from PyQt6 import QtWidgets
from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QApplication, QMainWindow


class ServerWindow(QMainWindow):
    def __init__(self):
        super(ServerWindow, self).__init__()
        loadUi('Screens\\Server.ui', self)
        ip = "127.0.0.1"
        port = 1234
        clients = 0
        self.server_ip.setText(ip)
        self.server_port.setText(str(port))
        self.server_clients.setText(str(clients))


class Server(object):
    def __init__(self, ip, port):
        self.server = ServerHandler()
    
    def run(self):
        while True:
            read_sockets, _, exception_sockets = select.select(self.server.sockets_list, [], self.server.sockets_list)
            for notified_socket in read_sockets:
                if notified_socket == self.server.server_socket:
                    client_socket, client_address = self.server.server_socket.accept()
                    user = self.server.receive_message(client_socket)
                    if user is False:
                        continue
                    self.server.sockets_list.append(client_socket)
                    self.server.clients[client_socket] = user
                    ip, port = client_address
                    print(f"\n[ USER CONNECTED: {user['data'].decode('utf-8')} ]\n"
                        f"[IP: {ip}]\n[Port: {port}]\n")
                else:
                    message = self.server.receive_message(notified_socket)
                    if message is False:
                        print(f"[ CONNECTION TERMINATED: {user['data'].decode('utf-8')} ]")
                        self.server.sockets_list.remove(notified_socket)
                        del self.server.clients[notified_socket]
                        continue
                    user = self.server.clients[notified_socket]
                    print(f"{user['data'].decode('utf-8')}  >> {message['data'].decode('utf-8')}")
                    for self.server.client_socket in self.server.clients:
                        if self.server.client_socket != notified_socket:
                            self.server.client_socket.send(user["header"] + user["data"] + message["header"] + message["data"])
            for notified_socket in exception_sockets:
                Server.sockets_list.remove(notified_socket)
                del self.server.clients[notified_socket]



if __name__ == "__main__":
    app = QApplication(sys.argv)
    screen = QtWidgets.QStackedWidget()
    server_window = ServerWindow()
    screen.setWindowTitle("Server running...")
    
    screen.addWidget(server_window)
    screen.setFixedHeight(590)
    screen.setFixedWidth(800)
    screen.show()
    sys.exit(app.exec())
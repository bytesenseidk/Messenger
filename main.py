import sys
from PyQt6 import QtWidgets
from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QApplication, QMainWindow


class Navigations(object):
    def connect_page(self):
        self.close()
        self.connect_screen = ConnectScreen()
        screens.addWidget(self.connect_screen)
        screens.setCurrentIndex(screens.currentIndex() + 1)

    def chat_page(self, username):
        self.close()
        self.chat_screen = ChatScreen(username)
        screens.addWidget(self.chat_screen)
        screens.setCurrentIndex(screens.currentIndex() + 1)
        
    def exit(self):
        sys.exit()
        

class ConnectScreen(QMainWindow, Navigations):
    def __init__(self):
        super(ConnectScreen, self).__init__()
        loadUi('Screens/Messenger_connect.ui', self)
        screens.setWindowTitle("Connect to chat")
        self.connect_button.clicked.connect(self.login)
        self.exit_button.clicked.connect(self.exit)
        

    def login(self):
        username = self.USER_ID.text()
        self.chat_page(username)


class ChatScreen(QMainWindow, Navigations):
    def __init__(self, username):
        self.username = username.split('@')[0]
        super(ChatScreen, self).__init__()
        loadUi('Screens/Messenger_chat.ui', self)
        screens.setWindowTitle("Ongoing chat..")
        self.disconnect_button.clicked.connect(self.connect_page)
        self.exit_button.clicked.connect(self.exit)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    screens = QtWidgets.QStackedWidget()
    main_window = ConnectScreen()
    
    screens.addWidget(main_window)
    screens.setFixedHeight(350)
    screens.setFixedWidth(800)
    screens.show()
    sys.exit(app.exec())
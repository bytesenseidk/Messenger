import sys
from PyQt6 import QtWidgets
from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QApplication, QMainWindow


class Navigations(object):
    def login_page(self):
        self.close()
        self.login_screen = LoginScreen()
        screens.addWidget(self.login_screen)
        screens.setCurrentIndex(screens.currentIndex() + 1)

    def welcome_page(self, username):
        self.close()
        self.welcome_screen = WelcomeScreen(username)
        screens.addWidget(self.welcome_screen)
        screens.setCurrentIndex(screens.currentIndex() + 1)
        
    def exit(self):
        sys.exit()
        

class LoginScreen(QMainWindow, Navigations):
    def __init__(self):
        super(LoginScreen, self).__init__()
        loadUi('Screens/Messenger_connect.ui', self)
        screens.setWindowTitle("Connect to chat")
        self.login_button.clicked.connect(self.login)
        self.exit_button.clicked.connect(self.exit)
        

    def login(self):
        username = self.USER_ID.text()
        self.welcome_page(username)


class WelcomeScreen(QMainWindow, Navigations):
    def __init__(self, username):
        self.username = username.split('@')[0]
        super(WelcomeScreen, self).__init__()
        loadUi('Screens/Messenger_chat.ui', self)
        screens.setWindowTitle("Ongoing chat..")
        self.logout_button.clicked.connect(self.login_page)
        self.exit_button.clicked.connect(self.exit)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    screens = QtWidgets.QStackedWidget()
    login_window = LoginScreen()
    
    screens.addWidget(login_window)
    screens.setFixedHeight(350)
    screens.setFixedWidth(800)
    screens.show()
    sys.exit(app.exec())
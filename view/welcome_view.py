from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QFrame, QMainWindow, QWidget, QGridLayout, QPushButton, QApplication, QVBoxLayout, QLineEdit
from PyQt5 import QtCore, QtGui, QtWidgets
from backend.user import verify_user



class WelcomeView(QWidget):
    switch_to_dashboard_page = pyqtSignal()

    def __init__(self, mainWindow):
        super().__init__()
        mainWindow.setObjectName("Home-page")
        mainWindow.resize(1922, 1048)
        self.layout = QVBoxLayout()
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setStyleSheet("QWidget{\n"
                                         "    background-color: rgb(41, 45, 57);}")
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(461, 300, 1000, 131))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel{\n"
                                 "    color: rgb(255, 255, 255);}")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.login_button = QtWidgets.QPushButton(self.centralwidget)
        self.login_button.setGeometry(QtCore.QRect(1700, 680, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.login_button.setFont(font)
        self.login_button.setStyleSheet("QPushButton{\n"
                                        "    background-color: rgb(32, 136, 245);\n"
                                        "    color: rgb(255, 255, 255);\n"
                                        "    border-radius: 15px;\n"
                                        "    font-weight: bold;\n"
                                        "}")
        self.login_button.setObjectName("pushButton_2")
        self.login_button.clicked.connect(self.switch_to_dashboard_page.emit)

        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 540, 1921, 101))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(500)
        self.gridLayout.setVerticalSpacing(50)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(100, -1, -1, -1)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel{\n"
                                   "    color: rgb(255, 255, 255);}")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.username_input = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.username_input.setFont(font)
        self.username_input.setStyleSheet("QLineEdit{\n"
                                          "    background-color: rgb(255, 255, 255);\n"
                                          "    border-radius:8px;\n"
                                          "    padding:10px;\n"
                                          "}")
        self.username_input.setObjectName("username_input")
        self.verticalLayout.addWidget(self.username_input)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(-1, -1, 100, -1)
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("QLabel{\n"
                                   "    color: rgb(255, 255, 255);}")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.password_input = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.password_input.setFont(font)
        self.password_input.setStyleSheet("QLineEdit{\n"
                                          "    background-color: rgb(255, 255, 255);\n"
                                          "    border-radius:8px;\n"
                                          "    padding:10px;\n"
                                          "}")
        self.password_input.setObjectName("password_input")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.verticalLayout_2.addWidget(self.password_input)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 1, 1, 1)
        mainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

        self.layout.addWidget(self.centralwidget)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Bienvenue au notre application de \n"
                                                    "gestion de consomation d\'electrecite"))
        self.login_button.setText(_translate("MainWindow", "Se connecter"))
        self.label_2.setText(_translate("MainWindow", "Username :"))
        self.label_3.setText(_translate("MainWindow", "Password :"))

    def verify_usr(self):
        username = self.username_input.text()
        password = self.password_input.text()
        try:
            if verify_user(username, password):
                return True

        except ValueError as er:
            return er

    def get_username(self):
        return self.username_input.text()

    def get_password(self):
        return self.password_input.text()


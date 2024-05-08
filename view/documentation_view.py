from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from backend.documentation import listDir, openFile, copyFile, deleteFile


def show_alert_box(msg):
    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Information)
    msg_box.setWindowTitle("Alert")
    msg_box.setText(msg)
    msg_box.exec_()


def show_delete_alert_box():
    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Question)
    msg_box.setText("Voulez vous vraiment effacer ce fichier?")
    msg_box.setWindowTitle("Confirmation")
    msg_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

    result = msg_box.exec_()
    if result == QMessageBox.Ok:
        return True
    else:
        return False

class DocumentationView(QWidget):

    switch_to_dashboard = pyqtSignal()
    switch_to_home_page = pyqtSignal()

    def __init__(self, mainWindow):
        super().__init__()
        mainWindow.setObjectName("MainWindow")
        mainWindow.resize(1922, 1048)
        self.layout = QVBoxLayout()
        self.centralwidget = QtWidgets.QWidget()
        self.centralwidget.setStyleSheet("QWidget{\n"
                                         "    background-color: rgb(53, 58, 69);}\n"
                                         "\n"
                                         "")
        self.centralwidget.setObjectName("centralwidget")
        self.logo_frame = QtWidgets.QFrame(self.centralwidget)
        self.logo_frame.setGeometry(QtCore.QRect(0, 0, 90, 90))
        self.logo_frame.setStyleSheet("QWidget{\n"
                                      "    background-color: rgb(32, 136, 245);}")
        self.logo_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.logo_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.logo_frame.setObjectName("logo_frame")
        self.top_widget = QtWidgets.QWidget(self.centralwidget)
        self.top_widget.setGeometry(QtCore.QRect(90, 0, 1832, 90))
        self.top_widget.setStyleSheet("QWidget{\n"
                                      "    background-color: rgb(41, 45, 57);}\n"
                                      "")
        self.top_widget.setObjectName("top_widget")
        self.page_title = QtWidgets.QLabel(self.top_widget)
        self.page_title.setGeometry(QtCore.QRect(0, 0, 1811, 90))
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.page_title.setFont(font)
        self.page_title.setStyleSheet("QLabel{\n"
                                      "    color: rgb(255, 255, 255);}")
        self.page_title.setAlignment(QtCore.Qt.AlignCenter)
        self.page_title.setObjectName("page_title")
        self.notifications_button = QtWidgets.QPushButton(self.top_widget)
        self.notifications_button.setGeometry(QtCore.QRect(1450, 30, 161, 28))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.notifications_button.setFont(font)
        self.notifications_button.setStyleSheet("QPushButton{\n"
                                                "    color: rgb(255, 255, 255);}")
        self.notifications_button.setFlat(True)
        self.notifications_button.setObjectName("notifications_button")
        self.logout_button = QtWidgets.QPushButton(self.top_widget)
        self.logout_button.setGeometry(QtCore.QRect(1622, 30, 181, 28))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.logout_button.setFont(font)
        self.logout_button.setStyleSheet("QPushButton{\n"
                                         "    color: rgb(255, 255, 255);}")
        self.logout_button.setFlat(True)
        self.logout_button.setObjectName("logout_button")
        self.logout_button.clicked.connect(self.switch_to_home_page.emit)

        self.menu_frame = QtWidgets.QFrame(self.centralwidget)
        self.menu_frame.setGeometry(QtCore.QRect(0, 90, 90, 961))
        self.menu_frame.setStyleSheet("QWidget{\n"
                                      "    background-color: rgb(41, 45, 57);}\n"
                                      "")
        self.menu_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.menu_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menu_frame.setObjectName("menu_frame")
        self.back_button = QtWidgets.QPushButton(self.menu_frame)
        self.back_button.setGeometry(QtCore.QRect(0, 10, 90, 79))
        self.back_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icons/back-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.back_button.setIcon(icon)
        self.back_button.setIconSize(QtCore.QSize(110, 110))
        self.back_button.setFlat(True)
        self.back_button.setObjectName("back_button")
        self.back_button.clicked.connect(self.switch_to_dashboard.emit)

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(110, 110, 1788, 918))
        self.frame.setMinimumSize(QtCore.QSize(0, 0))
        self.frame.setStyleSheet("background-color: rgb(41, 45, 57);\n"
                                 "border-radius:15px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        font = QtGui.QFont()
        font.setPointSize(20)

        self.addButton = QtWidgets.QPushButton(self.frame)
        self.addButton.move(1450, 30)
        self.addButton.setText("Add file")
        self.addButton.setFlat(True)
        self.addButton.setStyleSheet("color: rgb(255, 255, 255);")
        font.setUnderline(True)
        self.addButton.setFont(font)
        self.addButton.clicked.connect(self.addFile)

        self.deleteButton = QtWidgets.QPushButton(self.frame)
        self.deleteButton.move(1600, 30)
        self.deleteButton.setText("Delete file")
        self.deleteButton.setFlat(True)
        self.deleteButton.setStyleSheet("color: rgb(255, 255, 255);")
        self.deleteButton.setFont(font)
        self.deleteButton.clicked.connect(self.deleteFile)

        self.addPath = QtWidgets.QLineEdit(self.frame)
        self.addPath.setGeometry(QtCore.QRect(900, 30, 500, 40))
        font.setUnderline(False)
        font.setPointSize(16)
        self.addPath.setFont(font)
        self.addPath.setStyleSheet("QLineEdit{\n"
                                          "    background-color: rgb(255, 255, 255);\n"
                                          "    border-radius:8px;\n"
                                          "    padding:5px;\n"
                                          "}")

        self.frame_title = QtWidgets.QLabel(self.frame)
        self.frame_title.setGeometry(QtCore.QRect(30, 30, 241, 31))
        font.setPointSize(20)
        self.frame_title.setFont(font)
        self.frame_title.setStyleSheet("color: rgb(255, 255, 255);")
        self.frame_title.setObjectName("frame_title")
        mainWindow.setCentralWidget(self.centralwidget)
        self.loadDocumentationList()

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

        self.layout.addWidget(self.centralwidget)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.page_title.setText(_translate("MainWindow", "Tableau de bord"))
        self.notifications_button.setText(_translate("MainWindow", "Notifications"))
        self.logout_button.setText(_translate("MainWindow", "Deconnecter"))
        self.frame_title.setText(_translate("MainWindow", "Documentation :"))

    def addFile(self):
        try:
            path = r"%s" % self.addPath.text()
            if (path == ""):
                show_alert_box("chemin est vide")

            else:
                copyFile(path)
                self.addPath.setText(None)
                self.reloadList()

        except ValueError as e:
            show_alert_box("ficnier n'existe pas")

    def loadDocumentationList(self):
        self.documentation_list = QtWidgets.QListWidget(self.frame)
        self.documentation_list.setGeometry(QtCore.QRect(50, 100, 1691, 781))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.documentation_list.setFont(font)
        self.documentation_list.setLineWidth(3)
        self.documentation_list.setMidLineWidth(3)
        self.documentation_list.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.documentation_list.setAutoScrollMargin(16)
        self.documentation_list.setWordWrap(True)
        self.documentation_list.setStyleSheet("QListWidget::item { margin: 15px; color: rgb(255, 255, 255) }")
        self.documentation_list.addItems(listDir())
        self.documentation_list.setSortingEnabled(True)
        self.documentation_list.itemDoubleClicked.connect(self.openSelectedFile)

    def openSelectedFile(self):
        fileName = self.documentation_list.selectedItems()
        if fileName:
            fileName = fileName[0].text()
            openFile(fileName)
            self.documentation_list.clearSelection()


    def getSelectedFile(self):
        pass


    def reloadList(self):
        self.documentation_list.clear()
        self.documentation_list.addItems(listDir())



    def deleteFile(self):
        self.documentation_list.itemDoubleClicked.disconnect(self.openSelectedFile)
        self.deleteButton.setStyleSheet("color: rgb(0, 0, 255)")
        fileName = self.documentation_list.selectedItems()
        if fileName:
            confirmed = show_delete_alert_box()
            if confirmed:
                fileName = fileName[0].text()
                deleteFile(fileName)
                self.reloadList()
                self.deleteButton.setStyleSheet("color: rgb(255, 255, 255)")
                self.documentation_list.itemDoubleClicked.connect(self.openSelectedFile)












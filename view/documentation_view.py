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

    def __init__(self):
        super().__init__()
        self.setObjectName("MainWindow")
        self.setStyleSheet("background-color: rgb(41, 45, 57);")
        self.layout = QVBoxLayout()
        self.centralwidget = QtWidgets.QWidget()
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(0, 100))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame.setStyleSheet("background-color: rgb(41, 45, 57);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setMinimumSize(QtCore.QSize(110, 100))
        self.frame_5.setMaximumSize(QtCore.QSize(110, 100))
        self.frame_5.setStyleSheet("background-color: rgb(32, 136, 245);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_2.addWidget(self.frame_5)
        self.notifications_button = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.notifications_button.setFont(font)
        self.notifications_button.setStyleSheet("QPushButton{\n"
                                                "    color: rgb(255, 255, 255);}")
        self.notifications_button.setText("")
        self.notifications_button.setFlat(True)
        self.notifications_button.setObjectName("notifications_button")
        self.horizontalLayout_2.addWidget(self.notifications_button)
        self.page_title = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.page_title.setFont(font)
        self.page_title.setStyleSheet("QLabel{\n"
                                      "    color: rgb(255, 255, 255);}")
        self.page_title.setAlignment(QtCore.Qt.AlignCenter)
        self.page_title.setObjectName("page_title")
        self.horizontalLayout_2.addWidget(self.page_title)
        self.logout_button = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.logout_button.setFont(font)
        self.logout_button.setStyleSheet("QPushButton{\n"
                                         "    color: rgb(255, 255, 255);}")
        self.logout_button.setText("")
        self.logout_button.setFlat(True)
        self.logout_button.setObjectName("logout_button")
        self.horizontalLayout_2.addWidget(self.logout_button)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setMinimumSize(QtCore.QSize(110, 0))
        self.frame_3.setMaximumSize(QtCore.QSize(110, 16777215))
        self.frame_3.setStyleSheet("background-color: rgb(41, 45, 57);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.back_button = QtWidgets.QPushButton(self.frame_3)
        self.back_button.setGeometry(QtCore.QRect(12, 0, 86, 119))
        self.back_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icons/back-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.back_button.setIcon(icon)
        self.back_button.setIconSize(QtCore.QSize(110, 110))
        self.back_button.setFlat(True)
        self.back_button.setObjectName("back_button")
        self.horizontalLayout.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setStyleSheet("background-color: rgb(53, 58, 69);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_6 = QtWidgets.QFrame(self.frame_4)
        self.frame_6.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_6.setStyleSheet("background-color: rgb(41, 45, 57);\n"
                                   "border-radius:15px;")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_8 = QtWidgets.QFrame(self.frame_6)
        self.frame_8.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(300)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_title = QtWidgets.QLabel(self.frame_8)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setUnderline(True)
        self.frame_title.setFont(font)
        self.frame_title.setStyleSheet("color: rgb(255, 255, 255);")
        self.frame_title.setObjectName("frame_title")
        self.horizontalLayout_4.addWidget(self.frame_title)
        self.frame_9 = QtWidgets.QFrame(self.frame_8)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(20)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.addPath = QtWidgets.QLineEdit(self.frame_9)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.addPath.setFont(font)
        self.addPath.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                   "border-radius: 8px;\n"
                                   "padding: 5px;")
        self.addPath.setText("")
        self.addPath.setClearButtonEnabled(True)
        self.addPath.setObjectName("addPath")
        self.horizontalLayout_5.addWidget(self.addPath)
        self.addButton = QtWidgets.QPushButton(self.frame_9)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setUnderline(True)
        self.addButton.setFont(font)
        self.addButton.setStyleSheet("color: rgb(255, 255, 255);")
        self.addButton.setFlat(True)
        self.addButton.setObjectName("addButton")
        self.horizontalLayout_5.addWidget(self.addButton)
        self.deleteButton = QtWidgets.QPushButton(self.frame_9)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setUnderline(True)
        self.deleteButton.setFont(font)
        self.deleteButton.setStyleSheet("color: rgb(255, 255, 255);")
        self.deleteButton.setFlat(True)
        self.deleteButton.setObjectName("deleteButton")
        self.horizontalLayout_5.addWidget(self.deleteButton)
        self.horizontalLayout_4.addWidget(self.frame_9)
        self.verticalLayout_2.addWidget(self.frame_8)
        self.frame_7 = QtWidgets.QFrame(self.frame_6)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_2.addWidget(self.frame_7)
        self.horizontalLayout_3.addWidget(self.frame_6)
        self.horizontalLayout.addWidget(self.frame_4)
        self.verticalLayout.addWidget(self.frame_2)

        self.addButton.clicked.connect(self.addFile)
        self.deleteButton.clicked.connect(self.deleteFile)
        self.back_button.clicked.connect(self.switch_to_dashboard.emit)

        self.loadDocumentationList()

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

        self.layout.addWidget(self.centralwidget)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.page_title.setText(_translate("MainWindow", "Documentation"))
        self.frame_title.setText(_translate("MainWindow", "Documentation :"))
        self.addButton.setText(_translate("MainWindow", "Add file"))
        self.deleteButton.setText(_translate("MainWindow", "Delete file"))

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
        self.documentation_list = QtWidgets.QListWidget(self.frame_7)
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
        self.verticalLayout_4.addWidget(self.documentation_list)

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
        fileName = self.documentation_list.selectedItems()
        if fileName:
            self.documentation_list.itemDoubleClicked.disconnect(self.openSelectedFile)
            self.deleteButton.setStyleSheet("color: rgb(0, 0, 255)")
            confirmed = show_delete_alert_box()
            if confirmed:
                fileName = fileName[0].text()
                deleteFile(fileName)
                self.reloadList()
                self.deleteButton.setStyleSheet("color: rgb(255, 255, 255)")
                self.documentation_list.itemDoubleClicked.connect(self.openSelectedFile)

        else:
            show_alert_box("Choisissez un fichier")

import threading

from PyQt5.QtCore import pyqtSignal, Qt, QTimer, QCoreApplication
from PyQt5.QtWidgets import QFrame, QMainWindow, QWidget, QGridLayout, QPushButton, QApplication, QVBoxLayout
from PyQt5 import QtCore, QtGui, QtWidgets
from backend.plots import WeekPlots, MonthPlots, SixMonthPlots
from backend.snmp_protocole import snmp_get
from backend.dictionaries import oids, status_dic, source_dic
from pysnmp.hlapi import *


class DashboardView(QWidget):
    switch_to_consumption_page = pyqtSignal()
    switch_to_statistics_page = pyqtSignal()
    switch_to_onduleurs_page = pyqtSignal()
    switch_to_home_page = pyqtSignal()
    switch_to_documentation_page = pyqtSignal()
    counter = 0

    def __init__(self, mainWindow):
        super().__init__()
        mainWindow.setObjectName("Tableau de bord")
        mainWindow.setStyleSheet("QWidget{\n"
                                 "    background-color: rgb(53, 58, 69);}\n"
                                 "\n"
                                 "")
        self.layout = QVBoxLayout()
        self.mainWidget = QtWidgets.QWidget()
        self.mainWidget.setObjectName("frame")
        self.mainWidget.setGeometry(0, 0, 1922, 1048)
        self.logo_frame = QtWidgets.QFrame(self.mainWidget)
        self.logo_frame.setGeometry(QtCore.QRect(0, 0, 90, 90))
        self.logo_frame.setStyleSheet("QWidget{\n"
                                      "    background-color: rgb(32, 136, 245);}")
        self.logo_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.logo_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.logo_frame.setObjectName("logo_frame")
        self.main_frame = QtWidgets.QFrame(self.mainWidget)
        self.main_frame.setGeometry(QtCore.QRect(110, 100, 1801, 941))
        self.main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame.setObjectName("main_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.main_frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.consomation_onduleurs_frame = QtWidgets.QFrame(self.main_frame)
        self.consomation_onduleurs_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.consomation_onduleurs_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.consomation_onduleurs_frame.setObjectName("consomation_onduleurs_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.consomation_onduleurs_frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.consomation_frame = QtWidgets.QFrame(self.consomation_onduleurs_frame)
        self.consomation_frame.setStyleSheet("QFrame{\n"
                                             "    background-color: rgb(41, 45, 57);\n"
                                             "    border-radius:15px;\n"
                                             "}")
        self.consomation_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.consomation_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.consomation_frame.setObjectName("consomation_frame")
        self.consomation_title = QtWidgets.QLabel(self.consomation_frame)
        self.consomation_title.setGeometry(QtCore.QRect(10, 0, 221, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.consomation_title.setFont(font)
        self.consomation_title.setStyleSheet("QLabel{\n"
                                             "    color: rgb(255, 255, 255);}")
        self.consomation_title.setObjectName("consomation_title")
        self.consomation_analogue = QtWidgets.QLabel(self.consomation_frame)
        self.consomation_analogue.setGeometry(QtCore.QRect(30, 50, 369, 330))
        self.consomation_analogue.setText("")
        self.consomation_analogue.setPixmap(QtGui.QPixmap("../icons/analogue-icon.png"))
        self.consomation_analogue.setScaledContents(True)
        self.consomation_analogue.setObjectName("consomation_analogue")
        self.min_consumption_value = QtWidgets.QLabel(self.consomation_frame)
        self.min_consumption_value.setGeometry(QtCore.QRect(700, 221, 139, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.min_consumption_value.setFont(font)
        self.min_consumption_value.setStyleSheet("QLabel{\n"
                                                 "    color: rgb(255, 255, 255);}")
        self.min_consumption_value.setObjectName("min_consomation_value")
        self.max_label = QtWidgets.QLabel(self.consomation_frame)
        self.max_label.setGeometry(QtCore.QRect(491, 311, 179, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.max_label.setFont(font)
        self.max_label.setStyleSheet("QLabel{\n"
                                     "    color: rgb(255, 255, 255);}")
        self.max_label.setObjectName("max_label")
        self.valeure_label = QtWidgets.QLabel(self.consomation_frame)
        self.valeure_label.setGeometry(QtCore.QRect(491, 41, 131, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.valeure_label.setFont(font)
        self.valeure_label.setStyleSheet("QLabel{\n"
                                         "    color: rgb(255, 255, 255);}")
        self.valeure_label.setObjectName("valeure_label")
        self.consumption_value = QtWidgets.QLabel(self.consomation_frame)
        self.consumption_value.setGeometry(QtCore.QRect(700, 41, 139, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.consumption_value.setFont(font)
        self.consumption_value.setStyleSheet("QLabel{\n"
                                             "    color: rgb(255, 255, 255);}")
        self.consumption_value.setObjectName("consomation_value")
        self.moyene_label = QtWidgets.QLabel(self.consomation_frame)
        self.moyene_label.setGeometry(QtCore.QRect(491, 131, 151, 40))
        font.setPointSize(20)
        font.setBold(False)
        self.moyene_label.setFont(font)
        self.moyene_label.setStyleSheet("QLabel{\n"
                                        "    color: rgb(255, 255, 255);}")
        self.moyene_label.setObjectName("moyene_label")
        self.min_label = QtWidgets.QLabel(self.consomation_frame)
        self.min_label.setGeometry(QtCore.QRect(491, 221, 172, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.min_label.setFont(font)
        self.min_label.setStyleSheet("QLabel{\n"
                                     "    color: rgb(255, 255, 255);}")
        self.min_label.setObjectName("min_label")
        self.avrg_value = QtWidgets.QLabel(self.consomation_frame)
        self.avrg_value.setGeometry(QtCore.QRect(700, 131, 139, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.avrg_value.setFont(font)
        self.avrg_value.setStyleSheet("QLabel{\n"
                                      "    color: rgb(255, 255, 255);}")
        self.avrg_value.setObjectName("avrg_value")
        self.max_consumption_value = QtWidgets.QLabel(self.consomation_frame)
        self.max_consumption_value.setGeometry(QtCore.QRect(700, 311, 139, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.max_consumption_value.setFont(font)
        self.max_consumption_value.setStyleSheet("QLabel{\n"
                                                 "    color: rgb(255, 255, 255);}")
        self.max_consumption_value.setObjectName("max_consomation_value")
        self.horizontalLayout.addWidget(self.consomation_frame)
        self.source_onduleurs_frame = QtWidgets.QFrame(self.consomation_onduleurs_frame)
        self.source_onduleurs_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.source_onduleurs_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.source_onduleurs_frame.setObjectName("source_onduleurs_frame")
        self.source_frame = QtWidgets.QFrame(self.source_onduleurs_frame)
        self.source_frame.setGeometry(QtCore.QRect(12, -1, 851, 81))
        self.source_frame.setStyleSheet("QFrame{\n"
                                        "    background-color: rgb(41, 45, 57);\n"
                                        "border-radius:15px;}")
        self.source_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.source_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.source_frame.setObjectName("source_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.source_frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.source_label = QtWidgets.QLabel(self.source_frame)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.source_label.setFont(font)
        self.source_label.setStyleSheet("QLabel{\n"
                                        "    color: rgb(255, 255, 255);}")
        self.source_label.setObjectName("source_label")
        self.horizontalLayout_2.addWidget(self.source_label)
        self.source_type = QtWidgets.QLabel(self.source_frame)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.source_type.setFont(font)
        self.source_type.setStyleSheet("QLabel{\n"
                                       "    color: rgb(255, 255, 255);}")
        self.source_type.setObjectName("source_type")
        self.horizontalLayout_2.addWidget(self.source_type)
        self.onduleurs_frame = QtWidgets.QFrame(self.source_onduleurs_frame)
        self.onduleurs_frame.setGeometry(QtCore.QRect(12, 88, 851, 341))
        self.onduleurs_frame.setStyleSheet("QFrame{\n"
                                           "    background-color: rgb(41, 45, 57);\n"
                                           "border-radius:15px;}")
        self.onduleurs_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.onduleurs_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.onduleurs_frame.setObjectName("onduleurs_frame")
        self.onduleurs_title = QtWidgets.QLabel(self.onduleurs_frame)
        self.onduleurs_title.setGeometry(QtCore.QRect(10, 0, 221, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.onduleurs_title.setFont(font)
        self.onduleurs_title.setStyleSheet("QLabel{\n"
                                           "    color: rgb(255, 255, 255);}")
        self.onduleurs_title.setObjectName("onduleurs_title")
        self.puissance_analogue = QtWidgets.QLabel(self.onduleurs_frame)
        self.puissance_analogue.setGeometry(QtCore.QRect(30, 50, 333, 280))
        self.puissance_analogue.setText("")
        self.puissance_analogue.setPixmap(QtGui.QPixmap("../icons/analogue-icon.png"))
        self.puissance_analogue.setScaledContents(True)
        self.puissance_analogue.setObjectName("puissance_analogue")
        self.etats_label = QtWidgets.QLabel(self.onduleurs_frame)
        self.etats_label.setGeometry(QtCore.QRect(481, 131, 95, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.etats_label.setFont(font)
        self.etats_label.setStyleSheet("QLabel{\n"
                                       "    color: rgb(255, 255, 255);}")
        self.etats_label.setObjectName("etats_label")
        self.battery_value = QtWidgets.QLabel(self.onduleurs_frame)
        self.battery_value.setGeometry(QtCore.QRect(680, 131, 139, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.battery_value.setFont(font)
        self.battery_value.setStyleSheet("QLabel{\n"
                                         "    color: rgb(255, 255, 255);}")
        self.battery_value.setObjectName("battery_value")
        self.status_label = QtWidgets.QLabel(self.onduleurs_frame)
        self.status_label.setGeometry(QtCore.QRect(481, 221, 112, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.status_label.setFont(font)
        self.status_label.setStyleSheet("QLabel{\n"
                                        "    color: rgb(255, 255, 255);}")
        self.status_label.setObjectName("status_label")
        self.onduleurs_state = QtWidgets.QLabel(self.onduleurs_frame)
        self.onduleurs_state.setGeometry(QtCore.QRect(680, 221, 139, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.onduleurs_state.setFont(font)
        self.onduleurs_state.setStyleSheet("QLabel{\n"
                                           "    color: rgb(255, 255, 255);}")
        self.onduleurs_state.setObjectName("onduleurs_state")
        self.puissance_label = QtWidgets.QLabel(self.onduleurs_frame)
        self.puissance_label.setGeometry(QtCore.QRect(481, 41, 163, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.puissance_label.setFont(font)
        self.puissance_label.setStyleSheet("QLabel{\n"
                                           "    color: rgb(255, 255, 255);}")
        self.puissance_label.setObjectName("puissance_label")
        self.puissance_value = QtWidgets.QLabel(self.onduleurs_frame)
        self.puissance_value.setGeometry(QtCore.QRect(680, 41, 139, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.puissance_value.setFont(font)
        self.puissance_value.setStyleSheet("QLabel{\n"
                                           "    color: rgb(255, 255, 255);}")
        self.puissance_value.setObjectName("puissance_value")
        self.horizontalLayout.addWidget(self.source_onduleurs_frame)
        self.verticalLayout.addWidget(self.consomation_onduleurs_frame)
        self.frame_5 = QtWidgets.QFrame(self.main_frame)
        self.frame_5.setStyleSheet("QFrame{\n"
                                   "    background-color: rgb(41, 45, 57);\n"
                                   "    border-radius:15px;\n"
                                   "}")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")

        self.verticalLayout.addWidget(self.frame_5)
        self.menu_frame = QtWidgets.QFrame(self.mainWidget)
        self.menu_frame.setGeometry(QtCore.QRect(0, 90, 90, 961))
        self.menu_frame.setStyleSheet("QWidget{\n"
                                      "    background-color: rgb(41, 45, 57);}\n"
                                      "")
        self.menu_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.menu_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menu_frame.setObjectName("menu_frame")
        self.statistics_icon_button = QtWidgets.QPushButton(self.menu_frame)
        self.statistics_icon_button.setGeometry(QtCore.QRect(0, 340, 90, 79))
        self.statistics_icon_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icons/statistic-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.statistics_icon_button.setIcon(icon)
        self.statistics_icon_button.setIconSize(QtCore.QSize(70, 70))
        self.statistics_icon_button.setFlat(True)
        self.statistics_icon_button.setObjectName("dashboard_icon_button")
        self.statistics_icon_button.clicked.connect(self.switch_to_statistics_page.emit)

        self.statistics_button = QtWidgets.QPushButton(self.menu_frame)
        self.statistics_button.setGeometry(QtCore.QRect(0, 420, 90, 28))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.statistics_button.setFont(font)
        self.statistics_button.setStyleSheet("QPushButton{\n"
                                             "    color: rgb(255, 255, 255);}")
        self.statistics_button.setFlat(True)
        self.statistics_button.setObjectName("dashboard_button1")
        self.statistics_button.clicked.connect(self.switch_to_statistics_page.emit)

        self.consomation_icon_button = QtWidgets.QPushButton(self.menu_frame)
        self.consomation_icon_button.setGeometry(QtCore.QRect(0, 200, 90, 79))
        self.consomation_icon_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../icons/compeut-icon-png.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.consomation_icon_button.setIcon(icon1)
        self.consomation_icon_button.setIconSize(QtCore.QSize(70, 70))
        self.consomation_icon_button.setFlat(True)
        self.consomation_icon_button.setObjectName("consomation_icon_button")
        self.consomation_icon_button.clicked.connect(self.switch_to_consumption_page.emit)

        self.consomation_button = QtWidgets.QPushButton(self.menu_frame)
        self.consomation_button.setGeometry(QtCore.QRect(0, 280, 90, 28))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.consomation_button.setFont(font)
        self.consomation_button.setStyleSheet("QPushButton{\n"
                                              "    color: rgb(255, 255, 255);}")
        self.consomation_button.setFlat(True)
        self.consomation_button.setObjectName("consomation_button")
        self.consomation_button.clicked.connect(self.switch_to_consumption_page.emit)

        self.onduleurs_icon_button = QtWidgets.QPushButton(self.menu_frame)
        self.onduleurs_icon_button.setGeometry(QtCore.QRect(0, 480, 90, 79))
        self.onduleurs_icon_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../icons/onduleur-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.onduleurs_icon_button.setIcon(icon2)
        self.onduleurs_icon_button.setIconSize(QtCore.QSize(70, 70))
        self.onduleurs_icon_button.setFlat(True)
        self.onduleurs_icon_button.setObjectName("onduleurs_icon_button")
        self.onduleurs_icon_button.clicked.connect(self.switch_to_onduleurs_page.emit)

        self.onduleurs_buttons = QtWidgets.QPushButton(self.menu_frame)
        self.onduleurs_buttons.setGeometry(QtCore.QRect(0, 560, 90, 28))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.onduleurs_buttons.setFont(font)
        self.onduleurs_buttons.setStyleSheet("QPushButton{\n"
                                             "    color: rgb(255, 255, 255);}")
        self.onduleurs_buttons.setFlat(True)
        self.onduleurs_buttons.setObjectName("onduleurs_buttons")
        self.onduleurs_buttons.clicked.connect(self.switch_to_onduleurs_page.emit)

        self.top_widget = QtWidgets.QWidget(self.mainWidget)
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

        self.widget = QtWidgets.QWidget(self.top_widget)
        self.widget.setGeometry(QtCore.QRect(1240, 30, 553, 41))
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.documentation_button = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.documentation_button.setFont(font)
        self.documentation_button.setStyleSheet("QPushButton{\n"
                                                "    color: rgb(255, 255, 255);}")
        self.documentation_button.setFlat(True)
        self.documentation_button.setObjectName("documentation_button")
        self.documentation_button.clicked.connect(self.switch_to_documentation_page.emit)

        self.horizontalLayout_3.addWidget(self.documentation_button)
        self.notifications_button = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.notifications_button.setFont(font)
        self.notifications_button.setStyleSheet("QPushButton{\n"
                                                "    color: rgb(255, 255, 255);}")
        self.notifications_button.setFlat(True)
        self.notifications_button.setObjectName("notifications_button")
        self.horizontalLayout_3.addWidget(self.notifications_button)
        self.logout_button = QtWidgets.QPushButton(self.widget)
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
        self.horizontalLayout_3.addWidget(self.logout_button)
        self.show_statistics()
        self.updateLabels()
        mainWindow.setCentralWidget(self.mainWidget)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

        self.layout.addWidget(self.mainWidget)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

    def show_statistics(self):
        self.statistics_stackedWidget = QtWidgets.QStackedWidget(self.frame_5)
        self.statistics_stackedWidget.setGeometry(QtCore.QRect(0, 0, 1781, 671))
        self.statistics_stackedWidget.setObjectName("stackedWidget")

        self.week_statistiques_page = QtWidgets.QWidget()
        self.week_statistiques_page.setObjectName("week_statistiques_page")
        self.week_frame = QtWidgets.QFrame(self.week_statistiques_page)
        self.week_frame.setGeometry(QtCore.QRect(0, 0, 1781, 671))
        self.week_frame.setStyleSheet("QFrame{\n"
                                      "    background-color: rgb(41, 45, 57);\n"
                                      "    border-radius:15px;}")
        self.week_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.week_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.week_frame.setObjectName("week_frame")
        self.week_frame_title = QtWidgets.QLabel(self.week_frame)
        # self.week_frame_title.setGeometry(QtCore.QRect(10, 0, 191, 41))
        self.week_frame_title.move(10, 0)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.week_frame_title.setFont(font)
        self.week_frame_title.setStyleSheet("QLabel{\n"
                                            "    color: rgb(255, 255, 255);}")
        self.week_frame_title.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.week_frame_title.setObjectName("week_frame_title")
        self.week_label = QtWidgets.QLabel(self.week_frame)
        self.week_label.setGeometry(QtCore.QRect(830, 0, 123, 40))
        self.week_label.setAlignment(Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.week_label.setFont(font)
        self.week_label.setStyleSheet("QLabel{\n"
                                      "    color: rgb(255, 255, 255);}")
        self.week_label.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.week_label.setObjectName("week_label")

        self.week_plots_widget = QWidget(self.week_frame)
        self.week_plots_widget.setGeometry(QtCore.QRect(0, 40, 1700, 420))
        self.week_plots_widget.setStyleSheet("background-color: rgb(41, 45, 57);")

        self.week_plots = WeekPlots(parent=self.week_plots_widget)
        self.week_plots.setGeometry(QtCore.QRect(0, 0, 1700, 420))

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../Downloads/next-svgrepo-com (1).png"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)

        self.nextButton_1 = QtWidgets.QPushButton(self.week_frame)
        # self.nextButton_1.setGeometry(QtCore.QRect(968, 9, 33, 29))
        self.nextButton_1.move(955, 7)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../../../Downloads/next-svgrepo-com.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.nextButton_1.setIcon(icon1)
        self.nextButton_1.setFlat(True)
        self.nextButton_1.setObjectName("pushButton_2")
        self.nextButton_1.clicked.connect(self.next)
        self.statistics_stackedWidget.addWidget(self.week_statistiques_page)
        self.month_statistiques_page = QtWidgets.QWidget()
        self.month_statistiques_page.setObjectName("month_statistiques_page")
        self.month_frame = QtWidgets.QFrame(self.month_statistiques_page)
        self.month_frame.setGeometry(QtCore.QRect(0, 0, 1781, 671))
        self.month_frame.setStyleSheet("QFrame{\n"
                                       "    background-color: rgb(41, 45, 57);\n"
                                       "    border-radius:15px;}")
        self.month_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.month_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.month_frame.setObjectName("month_frame")
        self.month_frame_title = QtWidgets.QLabel(self.month_frame)
        # self.month_frame_title.setGeometry(QtCore.QRect(10, 0, 191, 41))
        self.month_frame_title.move(10, 0)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.month_frame_title.setFont(font)
        self.month_frame_title.setStyleSheet("QLabel{\n"
                                             "    color: rgb(255, 255, 255);}")
        self.month_frame_title.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.month_frame_title.setObjectName("month_frame_title")
        self.nextButton_2 = QtWidgets.QPushButton(self.month_frame)
        # self.nextButton_2.setGeometry(QtCore.QRect(978, 9, 33, 29))
        self.nextButton_2.move(955, 7)
        self.nextButton_2.setText("")
        self.nextButton_2.setIcon(icon1)
        self.nextButton_2.setFlat(True)
        self.nextButton_2.setObjectName("pushButton_9")
        self.nextButton_2.clicked.connect(self.next)
        self.backButton_2 = QtWidgets.QPushButton(self.month_frame)
        # self.backButton_2.setGeometry(QtCore.QRect(792, 9, 33, 29))
        self.backButton_2.move(797, 7)
        self.backButton_2.setText("")
        self.backButton_2.setIcon(icon)
        self.backButton_2.setFlat(True)
        self.backButton_2.setObjectName("pushButton_10")
        self.backButton_2.clicked.connect(self.back)
        self.month_label = QtWidgets.QLabel(self.month_frame)
        self.month_label.setGeometry(QtCore.QRect(830, 0, 123, 40))
        self.month_label.setAlignment(Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.month_label.setFont(font)
        self.month_label.setStyleSheet("QLabel{\n"
                                       "    color: rgb(255, 255, 255);}")
        self.month_label.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.month_label.setObjectName("week_label_5")
        self.month_plots_widget = QWidget(self.month_frame)
        self.month_plots_widget.setGeometry(QtCore.QRect(0, 40, 1700, 420))
        self.month_plots_widget.setStyleSheet("background-color: rgb(41, 45, 57);")

        self.month_plots = MonthPlots(parent=self.month_plots_widget)
        self.month_plots.setGeometry(QtCore.QRect(0, 0, 1700, 420))
        self.statistics_stackedWidget.addWidget(self.month_statistiques_page)
        self.six_months_statistiques = QtWidgets.QWidget()
        self.six_months_statistiques.setObjectName("six_months_statistiques")
        self.six_monthe_frame = QtWidgets.QFrame(self.six_months_statistiques)
        self.six_monthe_frame.setGeometry(QtCore.QRect(0, 0, 1781, 671))
        self.six_monthe_frame.setStyleSheet("QFrame{\n"
                                            "    background-color: rgb(41, 45, 57);\n"
                                            "    border-radius:15px;}")
        self.six_monthe_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.six_monthe_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.six_monthe_frame.setObjectName("six_monthe_frame")
        self.six_month_frame_title = QtWidgets.QLabel(self.six_monthe_frame)
        self.six_month_plots_widget = QWidget(self.six_monthe_frame)
        self.six_month_plots_widget.setGeometry(QtCore.QRect(0, 40, 1700, 420))
        self.six_month_plots_widget.setStyleSheet("background-color: rgb(41, 45, 57);")

        self.six_month_plots = SixMonthPlots(parent=self.six_month_plots_widget)
        self.six_month_plots.setGeometry(QtCore.QRect(0, 0, 1700, 420))
        # self.six_month_frame_title.setGeometry(QtCore.QRect(10, 0, 191, 41))
        self.six_month_frame_title.move(10, 0)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.six_month_frame_title.setFont(font)
        self.six_month_frame_title.setStyleSheet("QLabel{\n"
                                                 "    color: rgb(255, 255, 255);}")
        self.six_month_frame_title.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.six_month_frame_title.setObjectName("six_month_frame_title")
        self.six_month_label = QtWidgets.QLabel(self.six_monthe_frame)
        self.six_month_label.setGeometry(QtCore.QRect(830, 0, 123, 40))
        self.six_month_label.setAlignment(Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.six_month_label.setFont(font)
        self.six_month_label.setStyleSheet("QLabel{\n"
                                           "    color: rgb(255, 255, 255);}")
        self.six_month_label.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.six_month_label.setObjectName("six_month_label")

        self.backButton_3 = QtWidgets.QPushButton(self.six_monthe_frame)
        # self.backButton_3.setGeometry(QtCore.QRect(793, 9, 33, 29))
        self.backButton_3.move(790, 7)
        self.backButton_3.setText("")
        self.backButton_3.setIcon(icon)
        self.backButton_3.setFlat(True)
        self.backButton_3.setObjectName("pushButton_12")
        self.backButton_3.clicked.connect(self.back)
        self.statistics_stackedWidget.addWidget(self.six_months_statistiques)
        self.week_label.setText("Semaine")
        self.month_label.setText("1-Mois")
        self.six_month_label.setText("6-Mois")
        self.statistics_stackedWidget.setCurrentIndex(0)

    def next(self):
        self.counter += 1
        self.statistics_stackedWidget.setCurrentIndex(self.counter)

    def back(self):
        self.counter -= 1
        self.statistics_stackedWidget.setCurrentIndex(self.counter)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.consomation_title.setText(_translate("MainWindow", "Consomation :"))
        self.max_label.setText(_translate("MainWindow", "Maximume :"))
        self.valeure_label.setText(_translate("MainWindow", "Valeure :"))
        self.moyene_label.setText(_translate("MainWindow", "Moyenne :"))
        self.min_label.setText(_translate("MainWindow", "Minimume :"))
        self.source_label.setText(_translate("MainWindow", "Source :"))
        self.onduleurs_title.setText(_translate("MainWindow", "Onduleurs :"))
        self.etats_label.setText(_translate("MainWindow", "Etats :"))
        self.status_label.setText(_translate("MainWindow", "Status :"))
        self.puissance_label.setText(_translate("MainWindow", "Puissance :"))
        self.statistics_button.setText(_translate("MainWindow", "Statistiques"))
        self.consomation_button.setText(_translate("MainWindow", "Consomation"))
        self.onduleurs_buttons.setText(_translate("MainWindow", "Onduleurs"))
        self.page_title.setText(_translate("MainWindow", "Tableau de bord"))
        self.notifications_button.setText(_translate("MainWindow", "Notifications"))
        self.logout_button.setText(_translate("MainWindow", "Deconnecter"))
        self.documentation_button.setText(_translate("MainWindow", "Documentation"))

    timer = QTimer()
    min_consumption = snmp_get(oids.get("outputWatt"))
    max_consumption = snmp_get(oids.get("outputWatt"))
    totale_consumption = 0
    last_consumption = None
    last_source = None
    last_battery = None
    last_status = None

    def updateLabels(self):
        consumption = snmp_get(oids.get("outputWatt"))
        source = snmp_get(oids.get("source"))
        battery = snmp_get(oids.get("battery"))
        status = snmp_get(oids.get("status"))

        self.totale_consumption += float(consumption)
        self.consumption_value.setText("%s kW" % self.totale_consumption)
        self.consumption_value.adjustSize()

        if self.last_consumption != consumption:
            if consumption <= self.min_consumption:
                self.min_consumption = consumption
                print("min cons changed")

            if consumption > self.max_consumption:
                self.max_consumption = consumption
                print("max cons changed")




            self.max_consumption_value.setText("%s kW" % self.max_consumption)

            self.min_consumption_value.setText("%s kW" % self.min_consumption)

            self.avrg_value.setText("%s kW" % str((float(self.max_consumption) + float(self.min_consumption)) / 2.00))
            self.avrg_value.adjustSize()

        if self.last_source != source:
            self.source_type.setText(source_dic.get(source))
        # self.source_type.adjustSize()

        if self.last_consumption != consumption:
            self.puissance_value.setText("%s kW" % consumption)
            self.puissance_value.adjustSize()

        if self.last_battery != battery:
            self.battery_value.setText("%s %%" % battery)
            self.battery_value.adjustSize()

        if self.last_status != status:
            self.onduleurs_state.setText(status_dic.get(status))
            self.onduleurs_state.adjustSize()

        # if self.last_consumption != consumption or self.last_source != source or self.last_battery != battery or self.last_status != status:
        #     self.timer.timeout.connect(self.updateLabels)
        #     self.timer.start(10000)
        #     self.last_consumption = consumption
        #     self.last_source = source
        #     self.last_battery = battery
        #     self.last_status = status




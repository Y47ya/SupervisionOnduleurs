from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QStackedWidget, QMessageBox
from dashboard_view import DashboardView
from consumption_view import ConsumptionView
from statistics_view import StatisticsView
from onduleurs_view import OnduleursView
from welcome_view import WelcomeView
from documentation_view import DocumentationView
import sys


def show_alert_box(msg):
    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Information)
    msg_box.setWindowTitle("Alert")
    msg_box.setText(msg)
    msg_box.exec_()

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.usr_state = False
        self.myWindow = QMainWindow()
        self.myWindow.setGeometry(0, 0, 1922, 1048)

        self.dashboard = DashboardView(self.myWindow)
        self.consumption_page = ConsumptionView(self.myWindow)
        self.statistics_page = StatisticsView(self.myWindow)
        self.onduleurs_page = OnduleursView(self.myWindow)
        self.welcome_page = WelcomeView(self.myWindow)
        self.documentation_page = DocumentationView(self.myWindow)

        self.stackedWidget = QStackedWidget()
        self.stackedWidget.addWidget(self.dashboard)
        self.stackedWidget.addWidget(self.consumption_page)
        self.stackedWidget.addWidget(self.statistics_page)
        self.stackedWidget.addWidget(self.onduleurs_page)
        self.stackedWidget.addWidget(self.welcome_page)
        self.stackedWidget.addWidget(self.documentation_page)

        self.stackedWidget.setCurrentWidget(self.dashboard)

        self.myWindow.setCentralWidget(self.stackedWidget)

        self.dashboard.switch_to_consumption_page.connect(self.switch_to_consumption)
        self.dashboard.switch_to_statistics_page.connect(self.switch_to_statistics)
        self.dashboard.switch_to_onduleurs_page.connect(self.switch_to_onduleurs)
        self.dashboard.switch_to_home_page.connect(self.switch_to_home)
        self.dashboard.switch_to_documentation_page.connect(self.switch_to_documentation)

        self.consumption_page.switch_to_dashboard_page.connect(self.switch_to_dashboard)
        self.consumption_page.switch_to_statistics_page.connect(self.switch_to_statistics)
        self.consumption_page.switch_to_onduleurs_page.connect(self.switch_to_onduleurs)
        self.consumption_page.switch_to_home_page.connect(self.switch_to_home)

        self.statistics_page.switch_to_dashboard_page.connect(self.switch_to_dashboard)
        self.statistics_page.switch_to_consumption_page.connect(self.switch_to_consumption)
        self.statistics_page.switch_to_onduleurs_page.connect(self.switch_to_onduleurs)
        self.statistics_page.switch_to_home_page.connect(self.switch_to_home)

        self.onduleurs_page.switch_to_dashboard_page.connect(self.switch_to_dashboard)
        self.onduleurs_page.switch_to_statistics_page.connect(self.switch_to_statistics)
        self.onduleurs_page.switch_to_consumption_page.connect(self.switch_to_consumption)
        self.onduleurs_page.switch_to_home_page.connect(self.switch_to_home)

        self.welcome_page.switch_to_dashboard_page.connect(self.switch_to_dashboard_from_home)

        self.documentation_page.switch_to_dashboard.connect(self.switch_to_dashboard)
        self.documentation_page.switch_to_home_page.connect(self.switch_to_home)

        self.myWindow.show()

    def switch_to_dashboard(self):
            self.welcome_page.username_input.setText(None)
            self.welcome_page.password_input.setText(None)
            self.stackedWidget.setCurrentWidget(self.dashboard)

    def switch_to_dashboard_from_home(self):
        if self.verify_usr():
            self.welcome_page.username_input.setText(None)
            self.welcome_page.password_input.setText(None)
            self.stackedWidget.setCurrentWidget(self.dashboard)

    def switch_to_consumption(self):
        self.stackedWidget.setCurrentWidget(self.consumption_page)

    def switch_to_statistics(self):
        self.stackedWidget.setCurrentWidget(self.statistics_page)

    def switch_to_onduleurs(self):
        self.stackedWidget.setCurrentWidget(self.onduleurs_page)

    def switch_to_home(self):
        self.usr_state = False
        self.stackedWidget.setCurrentWidget(self.welcome_page)

    def switch_to_documentation(self):
        self.stackedWidget.setCurrentWidget(self.documentation_page)

    def verify_usr(self):
        user_name = self.welcome_page.get_username()
        pass_word = self.welcome_page.get_password()
        try:
            file = open("../users.txt", "r")
            for line in file:
                try:
                    username_password = line.split("|")
                    username = (username_password[0].split(":"))[1].strip()
                    password = (username_password[1].split(":"))[1].strip()

                    if username == user_name and password == pass_word:
                        self.usr_state = True
                        return True
                except:
                     show_alert_box("Verifier la forme d'utilisateur dans le fichier des utilisateurs")


            show_alert_box("Utilisateurs ou mot de passe invalide")
        except:
            show_alert_box("Fichier n'existe pas")

app = QApplication(sys.argv)
window = MyWindow()
sys.exit(app.exec_())
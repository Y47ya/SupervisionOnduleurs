import sys

from PyQt5.QtWidgets import QApplication, QMessageBox

from src.view.window import MyWindow

app = QApplication(sys.argv)
window = None

try:
    window = MyWindow()
except ValueError as e:
    alert_box = QMessageBox()
    alert_box.setWindowTitle("Erreur")
    alert_box.setText("Vérifiez la connexion avec les onduleurs")
    alert_box.exec_()
    if window:
        window.close()
    sys.exit(-1)

sys.exit(app.exec_())

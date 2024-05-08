import sys
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget

class StatisticsPlots(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.figure, self.ax = plt.subplots(constrained_layout=True)

        # Plot your data
        categories = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']
        self.ax.bar(categories, [8, 10, 11, 40, 20, 25, 35])

        # Create a canvas widget to display the plot
        self.canvas = FigureCanvas(self.figure)

        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Create a widget and add the MatplotlibWidget to it
    widget = QWidget()
    layout = QVBoxLayout()
    widget.setLayout(layout)
    matplotlib_widget = StatisticsPlots(parent=widget)  # Set widget as parent
    layout.addWidget(matplotlib_widget)

    widget.show()
    sys.exit(app.exec_())

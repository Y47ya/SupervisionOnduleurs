import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QVBoxLayout, QWidget
from src.backend.connection import get_connection


class WeekPlots(QWidget):
    def __init__(self):
        super().__init__()
        self.figure, self.ax = plt.subplots()
        self.plot()
        self.ax.spines['top'].set_visible(False)
        self.ax.spines['right'].set_visible(False)
        self.ax.spines['left'].set_visible(False)
        self.ax.spines['bottom'].set_color('#DDDDDD')
        self.ax.tick_params(bottom=False, left=False)
        self.ax.set_axisbelow(True)
        self.ax.yaxis.grid(True, color='#EEEEEE')
        self.ax.xaxis.grid(False)

        bar_color = self.bars[0].get_facecolor()
        for bar in self.bars:
            self.ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.3,
                         round(bar.get_height(), 1), horizontalalignment='center', color=bar_color, weight='bold')
        self.ax.set_facecolor((41 / 255, 45 / 255, 57 / 255))
        self.figure.patch.set_facecolor((41 / 255, 45 / 255, 57 / 255))
        self.canvas = FigureCanvas(self.figure)
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.setLayout(layout)

    def plot(self):
        mydb = get_connection()
        cursor = mydb.cursor()
        query = "select consomation, DATE_FORMAT(date_de_consomation, '%d-%m') from consomation where intervalle= '24h' order by date_de_consomation asc limit 7"
        cursor.execute(query)
        result = cursor.fetchall()
        dates = []
        consumptions = []
        for x in result:
            consumptions.append(x[0])
            dates.append(x[1])

        self.ax.tick_params(axis='x', colors='white')
        self.ax.tick_params(axis='y', colors='white')
        self.ax.set_ylabel('Consumption', color='white')
        self.ax.set_xlabel('Date', color='white')
        self.ax.set_xticks(range(len(dates)))
        self.ax.set_xticklabels(dates, rotation=45)

        plt.tight_layout()
        self.bars = self.ax.bar(dates, consumptions)


class MonthPlots(QWidget):
    def __init__(self):
        super().__init__()
        self.figure, self.ax = plt.subplots()
        self.plot()
        self.ax.spines['top'].set_visible(False)
        self.ax.spines['right'].set_visible(False)
        self.ax.spines['left'].set_visible(False)
        self.ax.spines['bottom'].set_color('#DDDDDD')
        self.ax.tick_params(bottom=False, left=False)
        self.ax.set_axisbelow(True)
        self.ax.yaxis.grid(True, color='#EEEEEE')
        self.ax.xaxis.grid(False)

        bar_color = self.bars[0].get_facecolor()
        for bar in self.bars:
            self.ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.3,
                         round(bar.get_height(), 1), horizontalalignment='center', color=bar_color, weight='bold')
        self.ax.set_facecolor((41 / 255, 45 / 255, 57 / 255))
        self.figure.patch.set_facecolor((41 / 255, 45 / 255, 57 / 255))
        self.canvas = FigureCanvas(self.figure)
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.setLayout(layout)

    def plot(self):
        mydb = get_connection()
        cursor = mydb.cursor()
        query = "select consomation, DATE_FORMAT(date_de_consomation, '%d-%m') from consomation where intervalle= 'week' order by date_de_consomation asc limit 4"
        cursor.execute(query)
        result = cursor.fetchall()
        dates = []
        consumptions = []
        for x in result:
            consumptions.append(x[0])
            dates.append(x[1])

        self.ax.tick_params(axis='x', colors='white')
        self.ax.tick_params(axis='y', colors='white')
        self.ax.set_ylabel('Consumption', color='white')
        self.ax.set_xlabel('Date', color='white')
        self.ax.set_xticks(range(len(dates)))
        self.ax.set_xticklabels(dates, rotation=45)

        plt.tight_layout()
        self.bars = self.ax.bar(dates, consumptions)


class SixMonthPlots(QWidget):
    def __init__(self):
        super().__init__()
        self.figure, self.ax = plt.subplots()
        self.plot()
        self.ax.spines['top'].set_visible(False)
        self.ax.spines['right'].set_visible(False)
        self.ax.spines['left'].set_visible(False)
        self.ax.spines['bottom'].set_color('#DDDDDD')
        self.ax.tick_params(bottom=False, left=False)
        self.ax.set_axisbelow(True)
        self.ax.yaxis.grid(True, color='#EEEEEE')
        self.ax.xaxis.grid(False)

        bar_color = self.bars[0].get_facecolor()
        for bar in self.bars:
            self.ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.3,
                         round(bar.get_height(), 1), horizontalalignment='center', color=bar_color, weight='bold')
        self.ax.set_facecolor((41 / 255, 45 / 255, 57 / 255))
        self.figure.patch.set_facecolor((41 / 255, 45 / 255, 57 / 255))
        self.canvas = FigureCanvas(self.figure)
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.setLayout(layout)

    def plot(self):
        mydb = get_connection()
        cursor = mydb.cursor()
        query = "select consomation, DATE_FORMAT(date_de_consomation, '%m') from consomation where intervalle= 'month'"
        cursor.execute(query)
        result = cursor.fetchall()
        dates = []
        consumptions = []
        for x in result:
            consumptions.append(x[0])
            dates.append(x[1])

        self.ax.tick_params(axis='x', colors='white')
        self.ax.tick_params(axis='y', colors='white')
        self.ax.set_ylabel('Consumption', color='white')
        self.ax.set_xlabel('Date', color='white')
        self.ax.set_xticks(range(len(dates)))
        self.ax.set_xticklabels(dates, rotation=45)

        plt.tight_layout()
        self.bars = self.ax.bar(dates, consumptions)

# def plot():
#     mydb = get_connection()
#     cursor = mydb.cursor()
#     query = "select consomation, DATE_FORMAT(date_de_consomation, '%d-%m') from consomation where intervalle= '24h' order by date_de_consomation asc limit 7"
#     cursor.execute(query)
#     result = cursor.fetchall()
#     dates = []
#     consumptions = []
#     for x in result:
#         consumptions.append(x[0])
#         dates.append(x[1])
#
#     fig, ax = plt.subplots()
#     bars = ax.bar(
#         dates, consumptions, color='lightblue'
#     )
#     ax.spines['top'].set_visible(False)
#     ax.spines['right'].set_visible(False)
#     ax.spines['left'].set_visible(False)
#     ax.spines['bottom'].set_color('#DDDDDD')
#
#     ax.tick_params(bottom=False, left=False)
#
#     ax.set_axisbelow(True)
#     ax.yaxis.grid(True, color='#EEEEEE')
#     ax.xaxis.grid(False)
#
#     bar_color = bars[0].get_facecolor()
#
#     for bar in bars:
#         ax.text(
#             bar.get_x() + bar.get_width() / 2,
#             bar.get_height() + 0.3,
#             round(bar.get_height(), 1),
#             horizontalalignment='center',
#             color=bar_color,
#             weight='bold'
#         )
#
#
#     ax.set_facecolor((41/255, 45/255, 57/255))
#     fig.patch.set_facecolor((41/255, 45/255, 57/255))
#     plt.show()
#
#
#








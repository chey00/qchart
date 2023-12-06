from PyQt6.QtWidgets import QMainWindow
from CentralWidget import CentralWidget
from DateTime import DateTime


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        #chart = CentralWidget(parent)
        chart = DateTime(parent)

        self.setCentralWidget(chart)

        self.setWindowTitle("Einführung in QCharts")
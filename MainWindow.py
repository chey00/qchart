from PyQt6.QtWidgets import QMainWindow
from CentralWidget import CentralWidget


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        chart = CentralWidget(parent)

        self.setCentralWidget(chart)

        self.setWindowTitle("Einführung in QCharts")
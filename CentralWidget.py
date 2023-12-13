from PyQt6.QtWidgets import QWidget, QSlider, QHBoxLayout, QGridLayout, QLabel

from DateTime import DateTime


class CentralWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.datetime = DateTime(parent)

        self.slider = QSlider()
        self.slider.setRange(-5, 5)
        self.slider.valueChanged.connect(self.datetime.add_value)

        layout = QHBoxLayout()

        layout.addWidget(self.datetime)
        layout.addWidget(self.slider)

        self.setLayout(layout)

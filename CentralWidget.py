from PyQt6.QtCharts import QLineSeries, QChart, QChartView, QSplineSeries, QValueAxis, QAbstractAxis
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget

# Package: PyQt6-Charts
class CentralWidget(QChartView):
    def __init__(self, parent=None):
        super().__init__(parent)

        chart = QChart()
        chart.setTitle("Die wunderbare Welt der Mathematik")

        axis_x = QValueAxis()
        axis_x.setRange(1, 4)

        axis_y = QValueAxis()
        axis_y.setRange(0, 10)

        chart.addAxis(axis_x, Qt.AlignmentFlag.AlignBottom)
        chart.addAxis(axis_y, Qt.AlignmentFlag.AlignRight)

        series = QSplineSeries()
        series.attachAxis(axis_x)
        series.attachAxis(axis_y)
        series.setName("Parabel")
        series.append(0, 0)
        series.append(1, 1)
        series.append(2, 4)
        series.append(3, 9)
        series.append(4, 16)
        series.append(5, 25)

        series2 = QLineSeries()
        series2.attachAxis(axis_x)
        series2.attachAxis(axis_y)
        series2.setName("Gerade")
        series2.append(0, -5)
        series2.append(1, -2.5)
        series2.append(2, 0)
        series2.append(3, 2.5)
        series2.append(4, 5)
        series2.append(5, 7.5)
        chart.addSeries(series)
        chart.addSeries(series2)

        self.setChart(chart)


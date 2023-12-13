from PyQt6.QtCharts import QLineSeries, QChart, QChartView, QSplineSeries, QValueAxis, QAbstractAxis, QDateTimeAxis
from PyQt6.QtCore import Qt, QDateTime, pyqtSlot


# Package: PyQt6-Charts
# https://github.com/chey00/qchart
class DateTime(QChartView):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.series = QSplineSeries()
        self.random_series = QLineSeries()

        chart = QChart()
        chart.setTitle("Die wunderbare Welt der Mathematik")
        chart.addSeries(self.series)

        self.date_time_axis = QDateTimeAxis()
        self.date_time_axis.setFormat("d.MM hh:mm")

        start_date_time = QDateTime().currentDateTime()

        end_date_time = QDateTime().currentDateTime().addSecs(5 * 60)

        self.date_time_axis.setRange(start_date_time, end_date_time)

        axis_y = QValueAxis()
        axis_y.setRange(-5, 5)

        chart.addAxis(self.date_time_axis, Qt.AlignmentFlag.AlignTop)
        chart.addAxis(axis_y, Qt.AlignmentFlag.AlignLeft)

        self.series.attachAxis(self.date_time_axis)
        self.series.attachAxis(axis_y)

        self.random_series.attachAxis(self.date_time_axis)
        self.random_series.attachAxis(axis_y)

        self.series.setName("Values from Slider")
        self.random_series.setName("Random Values")

        self.setChart(chart)

    @pyqtSlot(int)
    def add_value(self, value):
        current_time = QDateTime.currentDateTime()
        start_time = current_time.addSecs(-30)

        self.series.append(current_time.toMSecsSinceEpoch(), value)

        self.date_time_axis.setRange(start_time, current_time)

# Übungen
# 2) Erstellen Sie einen QTimer, welcher alle 10 Sekunden Zufallszahlen zwischen -5 und 5 generiert.
# 3) Erstellen Sie einen Slot add_random_value, welcher die Zufallszahlen mit der aktuellen Uhrzeit
#    der Serie aus 1) hinzufügt.
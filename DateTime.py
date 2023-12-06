from PyQt6.QtCharts import QLineSeries, QChart, QChartView, QSplineSeries, QValueAxis, QAbstractAxis, QDateTimeAxis
from PyQt6.QtCore import Qt, QDateTime
from PyQt6.QtWidgets import QWidget

# Package: PyQt6-Charts
# https://github.com/chey00/qchart
class DateTime(QChartView):
    def __init__(self, parent=None):
        super().__init__(parent)

        series = QSplineSeries()
        series2 = QLineSeries()

        chart = QChart()
        chart.setTitle("Die wunderbare Welt der Mathematik")
        chart.addSeries(series)
        chart.addSeries(series2)

        date_time_axis = QDateTimeAxis()
        date_time_axis.setFormat("d.MM hh:mm")

        start_date_time = QDateTime().currentDateTime()

        print(start_date_time)

        end_date_time = QDateTime().currentDateTime().addSecs(5 * 60)
        print(end_date_time)

        date_time_axis.setRange(start_date_time, end_date_time)

        axis_y = QValueAxis()
        axis_y.setRange(0, 10)

        chart.addAxis(date_time_axis, Qt.AlignmentFlag.AlignTop)

        chart.addAxis(axis_y, Qt.AlignmentFlag.AlignLeft)

        series2.attachAxis(date_time_axis)
        series2.attachAxis(axis_y)

        series.attachAxis(date_time_axis)
        series.attachAxis(axis_y)

        series.setName("Parabel")
        series.append(QDateTime.currentDateTime().toMSecsSinceEpoch(), 0)
        series.append(QDateTime.currentDateTime().addSecs(60).toMSecsSinceEpoch(), 1)
        series.append(QDateTime.currentDateTime().addSecs(120).toMSecsSinceEpoch(), 4)
        series.append(QDateTime.currentDateTime().addSecs(180).toMSecsSinceEpoch(), 9)
        series.append(QDateTime.currentDateTime().addSecs(240).toMSecsSinceEpoch(), 16)
        series.append(QDateTime.currentDateTime().addSecs(300).toMSecsSinceEpoch(), 25)

        series2.setName("Gerade")
        series2.append(QDateTime.currentDateTime().addSecs(60).toMSecsSinceEpoch(), 5)
        series2.append(QDateTime.currentDateTime().addSecs(120).toMSecsSinceEpoch(), 2.5)

        self.setChart(chart)

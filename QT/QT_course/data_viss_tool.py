import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QColorDialog
from PyQt5.QtCore import QSettings
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np

"""This is a data visualization tool example i got it from gpt"""
class DataVisualizationApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Data Visualization Dashboard')

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.layout.addWidget(self.canvas)

        self.button = QPushButton('Change Line Color', self)
        self.button.clicked.connect(self.change_line_color)
        self.layout.addWidget(self.button)

        self.settings = QSettings('MyCompany', 'DataVisualizationApp')

        self.plot()

    def plot(self):
        self.figure.clear()
        ax = self.figure.add_subplot(111)

        # Generate some data
        t = np.arange(0.0, 2.0, 0.01)
        s = np.sin(2 * np.pi * t)

        # Retrieve saved color setting
        color = self.settings.value('line_color', '#0000FF')

        ax.plot(t, s, color=color)
        self.canvas.draw()

    def change_line_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.settings.setValue('line_color', color.name())
            self.plot()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DataVisualizationApp()
    ex.show()
    sys.exit(app.exec_())

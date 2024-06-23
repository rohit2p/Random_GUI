import sys
import random
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMainWindow, QDialog, QVBoxLayout
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

# Load UI files
from main_window import Ui_MainWindow
from options_dialog import Ui_Dialog

class OptionsDialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(OptionsDialog, self).__init__(parent)
        self.setupUi(self)
        self.transparencySlider.setValue(20)  # Set default value to 20

    def get_transparency(self):
        return self.transparencySlider.value()

class MatplotlibCanvas(FigureCanvas):
    def __init__(self, parent=None):
        self.fig = Figure()
        self.ax = self.fig.add_subplot(111)
        super(MatplotlibCanvas, self).__init__(self.fig)
        self.setParent(parent)

        self.ax.set_xlim(0, 100)
        self.ax.set_ylim(0, 100)
        self.ax.set_aspect('equal')

    def draw_waypoint(self, x1, y1, x2, y2, transparency):
        self.ax.plot([x1, x2], [y1, y2], 'r-', alpha=transparency/100)
        self.draw()

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.transparency = 20  # Default transparency value
        self.optionButton.clicked.connect(self.open_options_dialog)
        self.createWaypointButton.clicked.connect(self.create_waypoint)

        self.canvas = MatplotlibCanvas(self)
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.mapView.setLayout(layout)

        self.waypoints = []

    def open_options_dialog(self):
        dialog = OptionsDialog(self)
        if dialog.exec_() == QDialog.Accepted:
            self.transparency = dialog.get_transparency()
            self.update_waypoints_transparency()

    def create_waypoint(self):
        # Create a waypoint as a line between two random points for demonstration
        x1, y1 = random.uniform(0, 100), random.uniform(0, 100)
        x2, y2 = random.uniform(0, 100), random.uniform(0, 100)
        self.waypoints.append((x1, y1, x2, y2))
        self.canvas.draw_waypoint(x1, y1, x2, y2, self.transparency)

    def update_waypoints_transparency(self):
        self.canvas.ax.clear()
        for x1, y1, x2, y2 in self.waypoints:
            self.canvas.draw_waypoint(x1, y1, x2, y2, self.transparency)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())

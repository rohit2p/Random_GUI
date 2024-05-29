import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
from appearance_dialog import MapAppearanceDialog  # Import the appearance dialog

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Main Window with Map')
        self.setGeometry(100, 100, 800, 600)

        # Main widget and layout
        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)
        self.layout = QVBoxLayout(self.main_widget)

        # Matplotlib figure and canvas
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.layout.addWidget(self.canvas)

        # Options button
        self.options_button = QPushButton("Options", self)
        self.options_button.clicked.connect(self.show_options_dialog)
        self.layout.addWidget(self.options_button)

        # Initial map plot
        self.update_map()

    def update_map(self, settings=None):
        self.figure.clear()
        ax = self.figure.add_subplot(111)

        # Dummy data for map
        x = np.linspace(-180, 180, 360)
        y = np.linspace(-90, 90, 180)
        X, Y = np.meshgrid(x, y)
        Z = np.sin(2 * np.pi * X / 360) * np.cos(2 * np.pi * Y / 180)

        if settings:
            if settings.get('draw_surface'):
                ax.contourf(X, Y, Z, cmap=settings.get('surface_color', 'viridis'))
            if settings.get('fill_water_bodies'):
                ax.contourf(X, Y, Z, cmap=settings.get('water_color', 'Blues'))
            if settings.get('fill_continents'):
                ax.contourf(X, Y, Z, cmap=settings.get('land_color', 'Greens'))
            if settings.get('draw_coastlines'):
                ax.plot(x, np.sin(2 * np.pi * x / 360) * 90, 'k-')
            if settings.get('draw_flight_track'):
                ax.plot(np.linspace(-180, 180, 50), np.linspace(-90, 90, 50), color=settings.get('vertices_color', 'red'))
            if settings.get('draw_marker'):
                ax.plot(0, 0, 'o', color=settings.get('waypoints_color', 'red'))
        else:
            ax.contourf(X, Y, Z, cmap='viridis')  # Default map

        self.canvas.draw()

    def show_options_dialog(self):
        dialog = MapAppearanceDialog(self)
        if dialog.exec_() == QDialog.Accepted:
            self.update_map(dialog.get_settings())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

import sys
from PyQt5.QtWidgets import QDialog, QColorDialog
from ui_map_appearance_dialog import Ui_MapAppearanceDialog

class MapAppearanceDialog(QDialog, Ui_MapAppearanceDialog):
    def __init__(self, parent=None):
        super(MapAppearanceDialog, self).__init__(parent)
        self.setupUi(self)

        self.water_color = 'Blues'
        self.land_color = 'Greens'
        self.surface_color = 'viridis'
        self.waypoints_color = 'red'
        self.vertices_color = 'red'

        self.btWaterColour.clicked.connect(self.choose_water_color)
        self.btLandColour.clicked.connect(self.choose_land_color)
        self.btWaypointsColour.clicked.connect(self.choose_waypoints_color)
        self.btSurfaceColour.clicked.connect(self.choose_vertices_color)
        self.btSurfaceColour.clicked.connect(self.choose_surface_color)

    def choose_color(self, button):
        color = QColorDialog.getColor()
        if color.isValid():
            button.setStyleSheet(f"background-color: {color.name()}")
            return color.name()
        return None

    def choose_water_color(self):
        color = self.choose_color(self.btWaterColour)
        if color:
            self.water_color = color

    def choose_land_color(self):
        color = self.choose_color(self.btLandColour)
        if color:
            self.land_color = color

    def choose_waypoints_color(self):
        color = self.choose_color(self.btWaypointsColour)
        if color:
            self.waypoints_color = color

    def choose_vertices_color(self):
        color = self.choose_color(self.btVerticesColour)
        if color:
            self.vertices_color = color

    def choose_surface_color(self):
        color = self.choose_color(self.btSurfaceColour)
        if color:
            self.surface_color = color

    def get_settings(self):
        return {
            'draw_graticule': self.cbDrawGraticule.isChecked(),
            'draw_coastlines': self.cbDrawCoastlines.isChecked(),
            'fill_water_bodies': self.cbFillWaterBodies.isChecked(),
            'fill_continents': self.cbFillContinents.isChecked(),
            'draw_marker': self.cbDrawMarker.isChecked(),
            'draw_flight_track': self.cbDrawFlightTrack.isChecked(),
            'draw_surface': self.cbDrawSurface.isChecked(),
            'water_color': self.water_color,
            'land_color': self.land_color,
            'surface_color': self.surface_color,
            'waypoints_color': self.waypoints_color,
            'vertices_color': self.vertices_color,
        }

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = MapAppearanceDialog()
    dialog.show()
    sys.exit(app.exec_())

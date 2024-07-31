import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QDialog, QGridLayout, QColorDialog)
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt

class CustomColorDialog(QDialog):
    def __init__(self, initial_color=QColor(), parent=None):
        super().__init__(parent)
        self.setWindowTitle('Custom Color Picker')
        self.setFixedSize(400, 300)
        
        self.selected_color = initial_color
        
        self.custom_colors = [
            '#e6194B', '#3cb44b', '#ffe119', '#4363d8', '#f58231',
            '#911eb4', '#42d4f4', '#f032e6', '#bfef45', '#fabed4',
            '#469990', '#dcbeff', '#9A6324', '#fffac8', '#800000',
            '#aaffc3', '#808000', '#ffd8b1', '#000075', '#a9a9a9',
            '#ffffff'
        ]

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        
        # Color swatches layout
        swatch_layout = QGridLayout()
        self.color_buttons = []
        for i, color in enumerate(self.custom_colors):
            button = QPushButton()
            button.setFixedSize(40, 40)
            button.setStyleSheet(f"background-color: {color}")
            button.clicked.connect(lambda _, col=color: self.set_selected_color(col))
            self.color_buttons.append(button)
            row = i // 5
            col = i % 5
            swatch_layout.addWidget(button, row, col)

        # Button to open QColorDialog
        self.color_picker_button = QPushButton('Pick Custom Color')
        self.color_picker_button.clicked.connect(self.open_color_picker)

        layout.addLayout(swatch_layout)
        layout.addWidget(self.color_picker_button)
        self.setLayout(layout)

    def set_selected_color(self, color):
        self.selected_color = QColor(color)
        self.accept()

    def open_color_picker(self):
        color = QColorDialog.getColor(self.selected_color, self, "Pick a Color")
        if color.isValid():
            self.selected_color = color
            self.accept()

    @staticmethod
    def getColor(initial_color=QColor(), parent=None, title="", options=QColorDialog.ColorDialogOptions()):
        dialog = CustomColorDialog(initial_color, parent)
        dialog.setWindowTitle(title)
        # dialog.setOptions(options)  # Removed this line
        if dialog.exec_() == QDialog.Accepted:
            return dialog.selected_color
        else:
            return QColor()  # Return an invalid color if the dialog is canceled

class ColorPickerApp(QWidget):
    def __init__(self):
        super().__init__()

        # Set up the main layout and button
        self.layout = QVBoxLayout()
        self.color_button = QPushButton('Pick a Color')
        self.color_button.clicked.connect(self.open_color_dialog)
        
        # Set up the label to display the chosen color
        self.color_display = QLabel('Chosen Color')
        self.color_display.setAlignment(Qt.AlignCenter)
        self.color_display.setFixedHeight(100)
        self.color_display.setStyleSheet("background-color: #ffffff")

        self.layout.addWidget(self.color_button)
        self.layout.addWidget(self.color_display)
        self.setLayout(self.layout)

    def open_color_dialog(self):
        color = CustomColorDialog.getColor()
        if color.isValid():
            self.color_display.setStyleSheet(f"background-color: {color.name()}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ColorPickerApp()
    window.setWindowTitle('Custom Color Picker')
    window.setFixedSize(400, 200)
    window.show()
    sys.exit(app.exec_())

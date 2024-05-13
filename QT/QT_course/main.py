from PyQt5.QtWidgets import QMainWindow, QLabel, QApplication
from PyQt5 import QtCore
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("This is first window from the course")

        label = QLabel("This is amazing")
        label.setAlignment(QtCore.Qt.AlignCenter)

        self.setCentralWidget(label)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
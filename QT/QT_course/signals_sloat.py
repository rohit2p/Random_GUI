# this was signal and slot an example

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from PyQt5 import QtCore
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.window_UI()

    def window_UI(self):
        # window
        self.setWindowTitle("Signals and slot")
        self.setFixedWidth(500)
        self.setFixedHeight(500)

        # lable
        self.label = QLabel(self)
        self.label.setText("UNCLICKED BUTTON")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.setCentralWidget(self.label)

        # button
        self.btn = QPushButton(self)
        self.btn.setText("Click me")
        self.btn.move(200, 300)
        self.btn.clicked.connect(self.on_btn_clicked) #signal

        self.show()

    # slot
    def on_btn_clicked(self):
        self.label.setText("CLICKED BUTTON")
        self.label.adjustSize()


app = QApplication(sys.argv)

window = MainWindow()

app.exec_()

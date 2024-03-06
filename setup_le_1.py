from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def function():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(850, 300, 300, 300)
    win.setWindowTitle("My first window by PyQt5")

    lable = QtWidgets.QLabel(win)
    lable.setText("My first text")
    lable.move(100, 100)

    win.show()
    sys.exit(app.exec_())

function()
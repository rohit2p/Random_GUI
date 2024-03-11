from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class Mywindow(QMainWindow):
    def __init__(self):
        super(Mywindow, self).__init__()
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle("Button 2")
        self.initUI()

    def initUI(self):
        self.lable = QtWidgets.QLabel(self)
        self.lable.setText("unclicked button")
        self.lable.move(105,50)

        self.button = QtWidgets.QPushButton(self)
        self.button.setText("click me")
        self.button.move(100, 100)
        self.button.clicked.connect(self.clicked)
    
    def clicked(self):
        self.lable.setText("you have clicked the button")
        self.update()
    
    def update(self):
        self.lable.adjustSize()
 

def window():
    app = QApplication(sys.argv)
    win = Mywindow()

    win.show()
    sys.exit(app.exec_())


window()
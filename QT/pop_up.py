from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QApplication
import sys

class Mywindow(QMainWindow):
    def __init__(self):
        super(Mywindow, self).__init__()
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle("window")
        self.lbl()
    
    def lbl(self):
        self.lable = QtWidgets.QLabel(self)
        self.lable.setText("Click me for pop-up")
        self.lable.adjustSize()
        self.lable.move(100, 100)

        self.button = QtWidgets.QPushButton("Click me", self)
        self.button.move(100, 130)
        self.button.clicked.connect(self.popup)


    def popup(self):
        msg = QMessageBox(self)
        msg.setWindowTitle("Pop-up")
        msg.setText("Want to change the lable?")
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Ok| QMessageBox.Cancel)

        msg.buttonClicked.connect(self.clicked_popup_check)

        msg.exec_() 

    def clicked_popup_check(self, r):
        if r.text() == "OK":
            self.lable.setText("you just changed the lable")
            self.lable.adjustSize()

def main():
    app = QApplication(sys.argv)
    win = Mywindow()
    
    win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
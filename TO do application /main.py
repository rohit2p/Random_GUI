import sqlite3
from PyQt5.QtWidgets import QWidget, QApplication, QListWidgetItem
from PyQt5 import QtCore
from PyQt5.uic import loadUi
import sys

class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        loadUi("main.ui", self)
        self.calendarWidget.selectionChanged.connect(self.calanderdateChanged)
        self.updateTaskList()

    def calanderdateChanged(self):
        dateSelected = self.calendarWidget.selectedDate().toPyDate()
        print("selected date: ", dateSelected)

    def updateTaskList(self):
        # for task in tasks:
        #     item = QListWidgetItem(task)
        #     item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
        #     item.setCheckState(QtCore.Qt.Unchecked)
        #     self.taskslistWidget.addItem(item)
        db = sqlite3.connect("data.db")
        cursor = db.cursor()

        query = "SELECT task, completed FROM tasks WHERE date = ?"
        row = (data)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
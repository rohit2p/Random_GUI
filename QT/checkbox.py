import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QListWidget, QListWidgetItem, QCheckBox
from PyQt5.QtCore import Qt  # Importing Qt from PyQt5.QtCore

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()

        self.selectAllCheckbox = QCheckBox("Select All")
        self.selectAllCheckbox.stateChanged.connect(self.selectAll)

        self.listWidget = QListWidget()

        # Adding items with checkboxes to the QListWidget
        for i in range(10):
            item = QListWidgetItem(f"Item {i + 1}")
            item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
            item.setCheckState(Qt.Unchecked)
            self.listWidget.addItem(item)

        self.layout.addWidget(self.selectAllCheckbox)
        self.layout.addWidget(self.listWidget)

        self.setLayout(self.layout)
        self.setWindowTitle('Select All Example')
        self.show()

    def selectAll(self, state):
        for i in range(self.listWidget.count()):
            item = self.listWidget.item(i)
            if state == Qt.Checked:
                item.setCheckState(Qt.Checked)
            else:
                item.setCheckState(Qt.Unchecked)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())

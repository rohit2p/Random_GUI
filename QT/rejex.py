import sys
import re
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QListWidget, QLabel

class RegexFilterApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Operation input
        self.operation_input = QLineEdit(self)
        self.operation_input.setPlaceholderText("Enter operation (e.g., name) and press Enter")
        layout.addWidget(self.operation_input)

        # List widget to display operations
        self.operations_list = QListWidget(self)
        layout.addWidget(self.operations_list)

        # Regex input
        self.regex_input = QLineEdit(self)
        self.regex_input.setPlaceholderText("Enter regex pattern")
        layout.addWidget(self.regex_input)

        # Apply button
        self.apply_button = QPushButton('Apply', self)
        self.apply_button.clicked.connect(self.apply_regex_filter)
        layout.addWidget(self.apply_button)

        # Filtered operations display
        self.filtered_list = QListWidget(self)
        layout.addWidget(self.filtered_list)

        self.setLayout(layout)
        self.setWindowTitle('Regex Filter Application')

        # Connect the operation input to add items to the operations list
        self.operation_input.returnPressed.connect(self.add_operation)

    def add_operation(self):
        operation = self.operation_input.text()
        if operation:
            self.operations_list.addItem(operation)
            self.operation_input.clear()

    def apply_regex_filter(self):
        regex_pattern = self.regex_input.text()
        self.filtered_list.clear()

        try:
            pattern = re.compile(regex_pattern)
        except re.error:
            self.filtered_list.addItem("Invalid regex pattern")
            return

        for index in range(self.operations_list.count()):
            operation = self.operations_list.item(index).text()
            if pattern.search(operation):
                self.filtered_list.addItem(operation)

def main():
    app = QApplication(sys.argv)
    ex = RegexFilterApp()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

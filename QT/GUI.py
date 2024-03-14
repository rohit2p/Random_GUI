import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QLabel, QGridLayout

class Crossword(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Crossword Game')

        # Create the grid layout for the crossword puzzle
        self.gridLayout = QGridLayout()

        # Create labels for the crossword puzzle
        self.labels = []
        for i in range(5):
            for j in range(5):
                label = QLabel()
                label.setAlignment(Qt.AlignCenter)
                label.setFixedSize(40, 40) # Adjust the size of each cell
                self.gridLayout.addWidget(label, i, j)
                self.labels.append(label)

        # Create the submit button
        self.submitButton = QPushButton('Submit')

        # Create the input line for the user to enter answers
        self.inputLine = QLineEdit()
        self.inputLine.setPlaceholderText('Enter your answer')
        
        # Create layout for input line and submit button
        self.inputLayout = QHBoxLayout()
        self.inputLayout.addWidget(self.inputLine)
        self.inputLayout.addWidget(self.submitButton)

        # Create the main layout
        self.mainLayout = QVBoxLayout()
        self.mainLayout.addLayout(self.gridLayout)
        self.mainLayout.addLayout(self.inputLayout)

        # Set the main layout for the window
        self.setLayout(self.mainLayout)

        # Set up connections
        self.submitButton.clicked.connect(self.checkAnswer)

        # Sample crossword puzzle data (dummy data)
        self.answers = {
            (0, 0): 'H',
            (0, 1): 'E',
            (0, 2): 'L',
            (0, 3): 'L',
            (0, 4): 'O',
            (1, 0): 'W',
            (1, 1): 'O',
            (1, 2): 'R',
            (1, 3): 'L',
            (1, 4): 'D',
            (2, 0): 'C',
            (2, 1): 'A',
            (2, 2): 'T',
            (2, 3): None, # Blank cell
            (2, 4): 'S',
            (3, 0): 'F',
            (3, 1): None, # Blank cell
            (3, 2): 'N',
            (3, 3): 'O',
            (3, 4): None, # Blank cell
            (4, 0): 'D',
            (4, 1): 'O',
            (4, 2): 'G',
            (4, 3): None, # Blank cell
            (4, 4): 'S'
        }

        # Initialize the crossword puzzle with empty strings
        self.initializePuzzle()

    def initializePuzzle(self):
        for i in range(5):
            for j in range(5):
                if (i, j) in self.answers:
                    answer = self.answers[(i, j)]
                    if answer is not None:
                        self.labels[i * 5 + j].setText(answer)
                    else:
                        self.labels[i * 5 + j].setText('')

    def checkAnswer(self):
        # Get user input from QLineEdit
        user_answer = self.inputLine.text().upper()
        
        # Check if user input matches any of the answers
        for pos, answer in self.answers.items():
            if answer is not None and answer == user_answer:
                row, col = pos
                self.labels[row * 5 + col].setStyleSheet("color: green; font-weight: bold")
        
        # Clear the input line after checking the answer
        self.inputLine.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    crossword = Crossword()
    crossword.show()
    sys.exit(app.exec_())

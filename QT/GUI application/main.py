import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QPushButton
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QPixmap, QCursor

wedgets = {
    'logo': [],
    'button': [],
    'score': [],
    'question':[]
}

app = QApplication(sys.argv)
window = QWidget()
window.setFixedWidth(1000)
window.setStyleSheet("background: #161219;")

# grid setup
grid = QGridLayout()

def frame1():
    # logo setup
    image = QPixmap("logo.png")
    logo = QLabel()
    logo.setPixmap(image)
    logo.setAlignment(QtCore.Qt.AlignCenter)
    logo.setStyleSheet("margin-top: 100px;")
    wedgets["logo"].append(logo)

    #button setup
    button = QPushButton("PLAY")
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button.setStyleSheet(
        "border: 4px solid '#BC006C'; " +
        "border-radius: 25px;" +
        "font-size: 35px;" +
        "margin: 100px 200px;" +
        "padding: 25px 0;" +
        "color: 'white'"
    )
    wedgets["button"].append(button)

    grid.addWidget(wedgets["logo"][-1], 0, 0)
    grid.addWidget(wedgets["button"][-1], 1, 0)

# frame1()

def frame2():
    score = QLabel()
    score.setAlignment(QtCore.Qt.AlignRight)
    wedgets["score"].append(score)
    score.setStyleSheet(
        "font-size: 35px;" +
        "color: 'white';" +
        "padding: 15px 10px 10px 10px;" +
        "margin: 20px 200px;" +
        "background: '#64a314';" +
        "border: 1px solid '#64a314';" +
        "border-radius: 30px;"
    )

    question = QLabel("This is the question??")
    question.setAlignment(QtCore.Qt.AlignCenter)
    wedgets["question"].append(question)
    question.setStyleSheet(
        "font-size: 25px;" +
        "color: 'white';" +
        "padding: 75px;"
    )

    grid.addWidget(wedgets["score"][-1], 0, 1)
    grid.addWidget(wedgets["question"][-1], 1, 0, 1, 2)



frame2()




window.setLayout(grid)

window.show()
sys.exit(app.exec())

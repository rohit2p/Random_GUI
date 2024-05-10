import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QPushButton
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QPixmap, QCursor

wedgets = {
    'logo': [],
    'button': [],
    'score': [],
    'question': [],
    'answer1': [],
    'answer2': [],
    'answer3': [],
    'answer4': [],
}

app = QApplication(sys.argv)
window = QWidget()
window.setFixedWidth(1000)
window.setStyleSheet("background: #161219;")

# grid setup
grid = QGridLayout()


def clear_widgets():
    for widget in wedgets:
        if wedgets[widget] != []:
            wedgets[widget][-1].hide()
        for i in range(0, len(wedgets[widget])):
            wedgets[widget].pop()


def start_game():
    clear_widgets()
    frame2()


def create_button(answer):
    button = QPushButton(answer)
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button.setFixedWidth(485)
    button.setStyleSheet(
        "QPushButton {"  # Target QPushButton specifically
        "border: 4px solid #23BC006C; "  # Corrected closing quote
        "color: white; "
        "font-family: 'shanti';"
        "font-size: 16px;"
        "border-radius: 25px;"
        "padding: 15px 0;"
        "margin-top: 20px;"
        "} "
        "QPushButton:hover {"  # Target hover state of QPushButton
        "background: '#BC006C';"
        "}"
    )
    return button


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
    button.clicked.connect(start_game)
    wedgets["button"].append(button)

    grid.addWidget(wedgets["logo"][-1], 0, 0)
    grid.addWidget(wedgets["button"][-1], 1, 0)


frame1()


def frame2():
    score = QLabel("20")
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

    button1 = create_button("answer1")
    button2 = create_button("answer2")
    button3 = create_button("answer3")
    button4 = create_button("answer4")

    wedgets['answer1'].append(button1)
    wedgets['answer2'].append(button2)
    wedgets['answer3'].append(button3)
    wedgets['answer4'].append(button4)

    image = QPixmap("logo.png")
    logo = QLabel()
    logo.setPixmap(image)
    logo.setAlignment(QtCore.Qt.AlignCenter)
    logo.setStyleSheet("margin-top: 100px; margin-bottom: 30px;")
    wedgets["logo"].append(logo)

    grid.addWidget(wedgets["score"][-1], 0, 1)
    grid.addWidget(wedgets["question"][-1], 1, 0, 1, 2)
    grid.addWidget(wedgets['answer1'][-1], 2, 0)
    grid.addWidget(wedgets['answer2'][-1], 2, 1)
    grid.addWidget(wedgets['answer3'][-1], 3, 0)
    grid.addWidget(wedgets['answer4'][-1], 3, 1)
    grid.addWidget(wedgets["logo"][-1], 4, 0, 1, 2)


# frame2()

window.setLayout(grid)

window.show()
sys.exit(app.exec())

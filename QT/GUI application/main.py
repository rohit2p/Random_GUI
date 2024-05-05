import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QPushButton
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QPixmap, QCursor

app = QApplication(sys.argv)
window = QWidget()
window.setFixedWidth(1000)
window.setStyleSheet("background: #161219;")

# grid setup
grid = QGridLayout()

# logo setup
image = QPixmap("logo.png")
logo = QLabel()
logo.setPixmap(image)
logo.setAlignment(QtCore.Qt.AlignCenter)
logo.setStyleSheet("margin-top: 100px;")

#button setup
button = QPushButton("PLAY")
button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
button.setStyleSheet(
    "border: 4px solid '#BC006C'; " +
    "border-radius: 15px;" +
    "font-size: 35px;" +
    "color: 'white'" +
    "padding: 25px 0" +
    "margin: 100px 200px"
)

grid.addWidget(logo, 0, 0)
grid.addWidget(button, 1, 0)
window.setLayout(grid)

window.show()
sys.exit(app.exec())

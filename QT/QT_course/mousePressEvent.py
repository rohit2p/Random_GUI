from PyQt5.QtWidgets import QApplication, QWidget

class MyWidget(QWidget):
    def mousePressEvent(self, event):
        print(f"Mouse button {event.button()} pressed at position {event.pos()}")

app = QApplication([])

widget = MyWidget()
widget.show()

app.exec_()

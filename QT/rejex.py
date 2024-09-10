import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QInputDialog
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class DraggableLegendPlot(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Draggable Legend Plot with Editable Text')
        self.setGeometry(100, 100, 800, 600)

        # Create the main widget and layout
        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)
        layout = QVBoxLayout(self.main_widget)

        # Create the Matplotlib figure and axes
        self.fig = Figure()
        self.ax = self.fig.add_subplot(111)

        # Create the FigureCanvas widget
        self.canvas = FigureCanvas(self.fig)
        layout.addWidget(self.canvas)

        # Plot some data
        self.plot_data()

        # Connect the legend to be draggable and clickable
        self.draggable_legend = None
        self.connect_legend()

    def plot_data(self):
        # Plot some example data
        self.ax.plot([0, 1, 2], [0, 1, 4], label='Quadratic')
        self.ax.plot([0, 1, 2], [0, 2, 3], label='Linear')
        self.ax.legend()

    def connect_legend(self):
        # Make the legend draggable
        self.legend = self.ax.legend()
        self.legend.set_draggable(True)

        # Connect the mouse press event
        self.canvas.mpl_connect('button_press_event', self.on_legend_click)

    def on_legend_click(self, event):
        # Check if the mouse click is within the legend
        if self.legend is None:
            return

        if self.legend.get_frame().contains(event)[0]:
            # Prompt user to update legend text
            items = [text.get_text() for text in self.legend.get_texts()]
            item, ok = QInputDialog.getItem(self, "Edit Legend Text", "Select item to edit:", items, 0, False)

            if ok and item:
                new_text, ok = QInputDialog.getText(self, "Edit Legend Text", "Enter new text:", text=item)
                if ok:
                    # Update the legend text
                    for text in self.legend.get_texts():
                        if text.get_text() == item:
                            text.set_text(new_text)
                    self.canvas.draw_idle()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DraggableLegendPlot()
    window.show()
    sys.exit(app.exec_())

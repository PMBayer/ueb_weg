from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QHBoxLayout, QWidget
from PyQt5.QtCore import Qt
import sys


class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        hbox = create_input_field()

        self.setLayout(hbox)
        self.setGeometry(750, 750, 800, 800)
        self.setWindowTitle('Gitterpotential Methode')


def create_input_field():
    # create & format HBox
    h_box = QHBoxLayout()
    h_box.setAlignment(Qt.AlignTop)

    #create & format Button
    input_dim = QPushButton('Enter')

    # create & format Layout
    enter_dim = QLabel('Dimension:')

    # create & format input field
    input_field = QtWidgets.QLineEdit()
    input_field.setValidator(QtWidgets.QIntValidator())
    input_field.setMaxLength(4)

    # adding widgets to layout
    h_box.addWidget(enter_dim)
    h_box.addWidget(input_dialog)
    h_box.addWidget(input_dim)

    return h_box


def create_grid(dim):
    pass


def main():
    # initialize Window
    app = QApplication(sys.argv)
    window = Window()

    # add input field for dimensions
    h_box = create_input_field()

    # Open Window
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

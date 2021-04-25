#!/usr/bin/env python

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QHBoxLayout, QWidget, QLineEdit, \
    QVBoxLayout, QGridLayout, QSpinBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
import sys


class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # create & modify Hbox for Input things
        self.hbox1 = QHBoxLayout()
        self.hbox1.setAlignment(Qt.AlignTop)

        # create & modify Dimension Label
        self.rows_label = QLabel('Rows: ')
        self.column_label = QLabel('Columns: ')

        # create & modify Textbox for Dimension
        self.rows_input = QSpinBox()
        self.column_input = QSpinBox()
        self.rows_input.setDisplayIntegerBase(10)
        self.column_input.setDisplayIntegerBase(10)

        # create & modify Button for entering Dimension
        self.enter_dim = QPushButton('Enter')
        self.enter_dim.clicked.connect(self.click_enter)

        # add widgets to hbox
        self.hbox1.addWidget(self.rows_label)
        self.hbox1.addWidget(self.rows_input)
        self.hbox1.addWidget(self.column_label)
        self.hbox1.addWidget(self.column_input)
        self.hbox1.addWidget(self.enter_dim)

        self.vbox = QVBoxLayout()
        self.grid = QGridLayout()

        self.hbox2 = QHBoxLayout()

        self.blockade = QPushButton('Block')
        self.start_point = QPushButton('Start')
        self.dest_point = QPushButton('Destination')
        self.find_path = QPushButton('Path')
        self.hbox2.addWidget(self.blockade)
        self.hbox2.addWidget(self.start_point)
        self.hbox2.addWidget(self.dest_point)
        self.hbox2.addWidget(self.find_path)

        # add every layout to vbox
        self.vbox.addLayout(self.hbox1)
        self.vbox.addLayout(self.grid)
        self.vbox.addLayout(self.hbox2)

        # general init of window
        self.setLayout(self.vbox)
        self.setGeometry(750, 750, 800, 800)
        self.setWindowTitle('Gitterpotential Methode')

    def create_grid(self):

        i = 1
        for row in range(self.rows_input.value()):
            for column in range(self.column_input.value()):
                button = QPushButton(str(i), row, column)
                self.grid.addWidget(button)
                i += 1

    def click_enter(self):
        self.create_grid()


def main():
    # initialize Window
    app = QApplication(sys.argv)
    window = Window()

    # Open Window
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

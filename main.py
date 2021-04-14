#!/usr/bin/env python

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QHBoxLayout, QWidget, QLineEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
import sys


class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # create & modify Hbox for Input things
        self.hbox = QHBoxLayout()
        self.hbox.setAlignment(Qt.AlignTop)

        # create & modify Dimension Label
        self.dim_label = QLabel('Dimension: ')

        # create & modify Textbox for Dimension
        self.textbox = QLineEdit()
        self.textbox.setValidator(QIntValidator())

        # create & modify Button for entering Dimension
        self.enter_dim = QPushButton('Enter')

        # add widgets to hbox
        self.hbox.addWidget(self.dim_label)
        self.hbox.addWidget(self.textbox)
        self.hbox.addWidget(self.enter_dim)

        # general init of window
        self.setLayout(self.hbox)
        self.setGeometry(750, 750, 800, 800)
        self.setWindowTitle('Gitterpotential Methode')


def create_grid(dim):
    pass


def main():
    # initialize Window
    app = QApplication(sys.argv)
    window = Window()

    # Open Window
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

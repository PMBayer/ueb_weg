#!/usr/bin/env python

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QHBoxLayout, QWidget, QLineEdit, \
    QVBoxLayout, QGridLayout, QSpinBox
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import *
import sys

import errors


class Window(QWidget):
    # Globals
    obstacle = False
    start = False
    destination = False
    coords = []

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
        self.grid.setColumnStretch(0, 0)
        self.hbox2 = QHBoxLayout()

        self.obstacle = QPushButton('Obstacle')
        self.obstacle.clicked.connect(self.click_obstacle)
        self.dest_point = QPushButton('Destination')
        self.dest_point.clicked.connect(self.click_dest)
        self.start_point = QPushButton('Start')
        self.start_point.clicked.connect(self.click_start)
        self.find_path = QPushButton('Path')
        self.find_path.clicked.connect(self.click_path)

        # adding buttons to Layout
        self.hbox2.addWidget(self.obstacle)
        self.hbox2.addWidget(self.dest_point)
        self.hbox2.addWidget(self.start_point)
        self.hbox2.addWidget(self.find_path)

        # add every layout to vbox
        self.vbox.addLayout(self.hbox1)
        self.vbox.addLayout(self.grid)
        self.vbox.addLayout(self.hbox2)

        # general init of window
        self.setLayout(self.vbox)
        self.setWindowTitle('Gitterpotential Methode')

    def create_grid(self):
        i = 0

        if 11 > self.rows_input.value() > 2 and 11 > self.column_input.value() > 2:
            for row in range(self.rows_input.value()):
                for column in range(self.column_input.value()):
                    coord = [row + 1, column + 1]
                    button = QPushButton(str(coord))
                    button.setCheckable(True)
                    button.setMinimumSize(QSize(50, 50))
                    button.setMaximumSize(QSize(50, 50))
                    self.coords.append(coord)
                    print(coord)
                    self.grid.addWidget(button, row + 1, column + 1)
                    button.clicked.connect(lambda: self.click_grid())
                    i += 1
        else:
            errors.grid_out_of_bounds_error()

    # Events
    def click_enter(self):
        self.create_grid()

    def click_obstacle(self):
        self.obstacle = True
        self.start = False
        self.destination = False
        print('Setting obstacles...')

    def click_start(self):
        self.start = True
        self.obstacle = False
        self.destination = False
        print('Setting start point...')

    def click_dest(self):
        self.destination = True
        self.obstacle = False
        self.start = False
        print('Setting destination...')

    def click_path(self):
        pass

    def click_grid(self):

        if self.obstacle == True:
            for index in range(len(self.coords)):
                coord = self.coords[index]
                print('loopin shit')
                if self.grid.itemAtPosition(coord[0], coord[1]).widget().isChecked():
                    print('r u doin sumthin')
                    print('Set obstacle at: ' + str(coord))
                    button = self.grid.itemAtPosition(coord[0], coord[1]).widget()
                    button.setStyleSheet("background-color: grey")
                    button.setText("Obstacle")
                    break

        if self.start == True:
            for index in range(len(self.coords)):
                coord = self.coords[index]
                print('loopin shit')
                if self.grid.itemAtPosition(coord[0], coord[1]).widget().isChecked():
                    print('r u doin sumthin')
                    print('Set obstacle at: ' + str(coord))
                    button = self.grid.itemAtPosition(coord[0], coord[1]).widget()
                    button.setStyleSheet("background-color: Green")
                    button.setText("Start")
                    break

        if self.destination == True:
            for index in range(len(self.coords)):
                coord = self.coords[index]
                if self.grid.itemAtPosition(coord[0], coord[1]).widget().isChecked():
                    print('Set obstacle at: ' + str(coord))
                    button = self.grid.itemAtPosition(coord[0], coord[1]).widget()
                    button.setStyleSheet("background-color: Green")
                    button.setText(str(0))
                    break

    def assign_button_number(self):
        # find start - e.g. find 0 in Grid
        for index in range(len(self.coords)):
            coord = self.coords[index]
            button = self.grid.itemAtPosition(coord[0], coord[1]).widget()
            if button.text() == str(0):
                dest_coord = coord
                print('This is the destination Coord: ' + str(dest_coord))

        # calculate surrounding numbers



def main():
    # initialize Window
    app = QApplication(sys.argv)
    window = Window()

    # Open Window
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

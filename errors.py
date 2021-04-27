import PyQt5
from PyQt5 import QtWidgets


def grid_out_of_bounds():
    error_dialog = QtWidgets.QErrorMessage()
    error_dialog.showMessage('Please choose  Values between 3 and 10')

    error_dialog.exec_()

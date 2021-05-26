import PyQt5
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox


def grid_out_of_bounds_error():
    error_dialog = QtWidgets.QMessageBox()
    error_dialog.setIcon(QMessageBox.Critical)
    error_dialog.setText('Error!')
    error_dialog.setInformativeText('Please choose Values between 3 and 10')
    error_dialog.setWindowTitle('Error!')

    error_dialog.exec_()


def cant_find_path_error():
    error_dialog = QtWidgets.QMessageBox()
    error_dialog.setIcon(QMessageBox.Critical)
    error_dialog.setText('Error!')
    error_dialog.setInformativeText('Cant find path from Start to Destination. \n Please adjust your Grid.')
    error_dialog.setWindowTitle('Error!')

    error_dialog.exec_()





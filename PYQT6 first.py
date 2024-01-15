from PyQt6.QtWidgets import QMessageBox
import PyQt6.QtWidgets as qtw
import PyQt6.QtCore as qtc
import PyQt6.QtGui as qtg


class MainWindow(qtw.QMainWindow):

    def quit(self):
        dialog  = QMessageBox.warning(self, "Quit", "Are you sure",
                                QMessageBox.StandardButton.Ok |
                                  QMessageBox.StandardButton.Cancel)
        if dialog == QMessageBox.Ok:
            self.close()
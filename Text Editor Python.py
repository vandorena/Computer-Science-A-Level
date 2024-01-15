import PyQt6.QtWidgets as qtw
import PyQt6.QtCore as qtc
import PyQt6.QtGui as qtg

class Window(qtw.QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Text Editor - AVD")
        self.resize(1900,1070)
        #layout_1 = qtw.QGraphicsGridLayout
        
        #layout_1.columnCount(layout_1)
        layout = qtw.QBoxLayout
        layout_2 = qtw.QFormLayout
        self.setCentralWidget()



app = qtw.QApplication([])
window = Window()
window.show()
app.exec()
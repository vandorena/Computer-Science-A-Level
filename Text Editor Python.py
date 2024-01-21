import PyQt6.QtWidgets as qtw
import PyQt6.QtCore as qtc
import PyQt6.QtGui as qtg
import this

class Window(qtw.QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Text Editor - AVD")
        self.resize(1000,700)
        #layout_1 = qtw.QGraphicsGridLayout
        
        #layout_1.columnCount(layout_1)
        layout = qtw.QGridLayout()
        self.open_button = qtw.QPushButton(text="Open")
        self.open_button.clicked.connect(self.open_button_fc)
        layout.addWidget(self.open_button, 0, 2)

        self.poem_button = qtw.QPushButton(text="Poem")
        self.poem_button.clicked.connect(self.poem_funct)
        layout.addWidget(self.poem_button, 0, 0)

        self.main_text = qtw.QTextEdit()
        text = self.main_text.toPlainText()
        self.main_text.setPlainText(text)
        layout.addWidget(self.main_text,0,1)

        widget = qtw.QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def poem_funct(self):
        self.main_text.setPlainText(print(this.))

    def open_button_fc(self):
        #print("Button Clicked")
        filename, _ = qtw.QFileDialog.getOpenFileName(self, "Open File", ".", "Text Files (*.txt)")
        #if filename:
            #read_text = 




app = qtw.QApplication([])
window = Window()
window.show()
app.exec()


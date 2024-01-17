import PyQt6.QtWidgets as qtw
import PyQt6.QtCore as qtc
import PyQt6.QtGui as qtg


# Subclass QMainWindow to customise your application's main window
class MainWindow(qtw.QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Layout Demo")

        layout = qtw.QVBoxLayout()
        #
        layout2 = qtw.QFormLayout()
        self.lineEdit = qtw.QLineEdit()
        self.lineEdit.setValidator(qtg.QDoubleValidator())
        layout2.addRow("Feet", self.lineEdit)
        self.label = qtw.QLabel()
        layout2.addRow("Metres:", self.label)
        #
        layout.addLayout(layout2)
        
        self.quitButton = qtw.QPushButton(text = "Quit")
        self.quitButton.clicked.connect(self.quit)
        layout.addWidget(self.quitButton)


        self.pushButton = qtw.QPushButton(text="Go")
        self.pushButton.clicked.connect(self.changeText)
        layout.addWidget(self.pushButton)

        self.saveButton = qtw.QPushButton(text= "L bOzO")
        self.saveButton.clicked.connect(self.open_btn)
        layout.addWidget(self.saveButton)
        
        widget = qtw.QWidget()
        widget.setLayout(layout)
        
        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)

    def changeText(self):
        if self.lineEdit.text():
            self.label.setText(str(float(self.lineEdit.text())*0.3048))
    
    def quit(self):
        dialog = qtw.QMessageBox.critical(self,"Quit", "Are you sure?", qtw.QMessageBox.StandardButton.Ok | qtw.QMessageBox.StandardButton.Cancel)
        if dialog == qtw.QMessageBox.StandardButton.Ok:
            self.close()

    def open_btn(self):
        filename, _ = qtw.QFileDialog.getOpenFileName(self, "Open File", ".", "Text Files (*.txt *.html)")
        print(filename)
        delp = qtw.QMessageBox.question(self, "Acknowledge" , qtw.QMessageBox.StandardButton.Abort)
        if delp == qtw.QMessageBox.StandardButton.Abort:
            self.close()
        

# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
app = qtw.QApplication([])

window = MainWindow()
window.show()

# Start the event loop.
app.exec()


# Your application won't reach here until you exit and the event 
# loop has stopped.
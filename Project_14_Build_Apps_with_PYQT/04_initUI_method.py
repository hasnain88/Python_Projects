from PyQt6.QtWidgets import QWidget,QApplication,QLabel, QPushButton
from PyQt6.QtGui import QPixmap
import sys

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.count = 0
        self.setWindowTitle("My First PyQT Window")
        self.setGeometry(0,0,400,300)
        
        ## To Create a button
        button = QPushButton(self)
        button.setText("Click Here")
        button.move(100,200)
        button.clicked.connect(self.buttonClicked)

        ## Adding lable to display count
        self.label = QLabel(self)
        self.label.setText("0")
        self.label.move(100,150)
    
    def buttonClicked(self):
        print("Button is clicked")
        self.count+=1
        self.label.setText(str(self.count))
        self.label.adjustSize()
        



app = QApplication(sys.argv)
window = Window()
window.show()


sys.exit(app.exec())

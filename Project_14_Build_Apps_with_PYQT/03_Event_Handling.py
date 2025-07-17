from PyQt6.QtWidgets import QWidget,QApplication,QLabel, QPushButton
from PyQt6.QtGui import QPixmap
import sys

class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("My First PyQT Window")
        self.setGeometry(0,0,400,300)
        
        ## To Create a button
        button = QPushButton(self)
        button.setText("Click Here")
        button.move(100,200)
        button.clicked.connect(self.buttonClicked)
    
    def buttonClicked(self):
        print("Button is clicked")



app = QApplication(sys.argv)
window = Window()
window.show()


sys.exit(app.exec())

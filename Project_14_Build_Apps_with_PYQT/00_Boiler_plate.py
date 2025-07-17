from PyQt6.QtWidgets import QWidget,QApplication,QLabel, QPushButton, QLineEdit
from PyQt6.QtGui import QPixmap
import sys

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.count = 0
        self.setWindowTitle("My First PyQT Window")
        self.setGeometry(0,0,400,150)

       



app = QApplication(sys.argv)
window = Window()
window.show()


sys.exit(app.exec())

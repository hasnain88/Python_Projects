from PyQt6.QtWidgets import QWidget,QApplication,QLabel, QPushButton, QLineEdit,QStyleFactory,QVBoxLayout
from PyQt6.QtGui import QPixmap
import sys

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0,0,700,150)
        label = QLabel("<h1><font color='red'>This is a label</h1>",self)
        label.resize(200,50)
        layout = QVBoxLayout()
        layout.addWidget(label)
        self.setLayout(layout)
        

       



app = QApplication(sys.argv)
# app.setStyle("windows11")
window = Window()
# print(QStyleFactory.keys())
# print(app.style().name())
window.show()


sys.exit(app.exec())

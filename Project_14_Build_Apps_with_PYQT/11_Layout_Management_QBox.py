from PyQt6.QtWidgets import QWidget,QApplication,QLabel, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt6.QtWidgets import QLineEdit,QCheckBox,QMessageBox,QMainWindow
from PyQt6.QtGui import QPixmap
import sys
import math

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.count = 0
        self.setWindowTitle("My First PyQT Window")
        self.setGeometry(0,0,400,150)
    
        label = QLabel("Name")
        name = QLineEdit()
        button = QPushButton("Add")

        layout = QHBoxLayout()
        layout.addWidget(label)
        layout.addWidget(name)
        layout.addWidget(button)
        self.setLayout(layout)

        # layout = QVBoxLayout()
        # layout.addWidget(label)
        # layout.addWidget(name)
        # layout.addWidget(button)
        # self.setLayout(layout)
      
                    


        

app = QApplication(sys.argv)
window = Window()
window.show()


sys.exit(app.exec())

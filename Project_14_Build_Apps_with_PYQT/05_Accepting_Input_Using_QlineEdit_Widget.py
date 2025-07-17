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
        self.setGeometry(0,0,300,200)

        # 
        name_label = QLabel(self)
        name_label.setText("Enter your name")
        name_label.move(60,10)

        self.name = QLineEdit(self)
        self.name.resize(200,20)
        self.name.move(60,50)

        button = QPushButton(self)
        button.setText("Add")
        button.move(200,80)
        button.clicked.connect(self.buttoncliked)

        self.result_label = QLabel(self)
        self.result_label.setFixedSize(150,220)
        self.move(160,120)
    
    def buttoncliked(self):
        # print("Button Clicked...")
        # print(f"Your name is {self.name.text()}")
        self.result_label.setText(f"Your name is {self.name.text()}")


        

        



app = QApplication(sys.argv)
window = Window()
window.show()


sys.exit(app.exec())

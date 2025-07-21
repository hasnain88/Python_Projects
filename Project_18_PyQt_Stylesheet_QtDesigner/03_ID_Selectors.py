from PyQt6.QtWidgets import QWidget,QApplication,QLabel, QPushButton, QLineEdit,QStyleFactory,QVBoxLayout
from PyQt6.QtGui import QPixmap
import sys

stylesheet="""
    QPushButton#My_Button{
    background-color:grey;
    padding:5px;
        }

    QPushButton#My_Button:pressed{
    background-color:blue;
    padding:5px;
        }

    QLabel#My-Label{
    background-color:red;
    color:white;
    margin:100px;
        }
    
"""

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0,0,700,150)
        label = QLabel("<h1>This is a label</h1>",self)
        label.setObjectName("My-Label")
        label.resize(200,50)
        button=QPushButton("Click here")
        button.setObjectName("My_Button")
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(button)
        self.setLayout(layout)
        

       



app = QApplication(sys.argv)
app.setStyleSheet(stylesheet)
window = Window()
window.show()
sys.exit(app.exec())

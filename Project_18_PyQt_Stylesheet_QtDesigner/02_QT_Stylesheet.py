from PyQt6.QtWidgets import QWidget,QApplication,QLabel, QPushButton, QLineEdit,QStyleFactory,QVBoxLayout
from PyQt6.QtGui import QPixmap
import sys

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0,0,700,150)
        label = QLabel("<h1>This is a label</h1>",self)
        label.resize(200,50)
        label.setStyleSheet("""
                            background-color:red;
                            color:white;
                            margin:100px;
                            """)
        button=QPushButton("Click here")
        button.setStyleSheet("""
                            QPushButton{
                             background-color:grey;
                             padding:5px;
                             }
                             QPushButton:pressed{
                             background-color:blue;
                             padding:5px;
                             }
                             """)

        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(button)
        self.setLayout(layout)
        

       



app = QApplication(sys.argv)
# app.setStyle("windows11")
window = Window()
# print(QStyleFactory.keys())
# print(app.style().name())
window.show()


sys.exit(app.exec())

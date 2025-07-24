from PyQt6.QtWidgets import QWidget,QApplication,QLabel, QPushButton, QLineEdit,QListWidget,QListWidgetItem,QHBoxLayout
from PyQt6.QtGui import QPixmap
import sys

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.count = 0
        self.setWindowTitle("Databases")
        self.setGeometry(0,0,400,150)

        fruits = ['Apple','Mango','Banana','Pineapple']
       
        self.listWidget = QListWidget()
        self.listWidget.setAlternatingRowColors(True)
        for fruit in fruits:
            listitem = QListWidgetItem()
            listitem.setText(fruit)
            self.listWidget.addItem(listitem)

        self.layout = QHBoxLayout()
        self.layout.addWidget(self.listWidget)
        self.setLayout(self.layout)
       





app = QApplication(sys.argv)
window = Window()
window.show()


sys.exit(app.exec())

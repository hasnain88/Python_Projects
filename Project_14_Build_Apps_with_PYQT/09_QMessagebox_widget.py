from PyQt6.QtWidgets import QWidget,QApplication,QLabel, QPushButton
from PyQt6.QtWidgets import QLineEdit,QCheckBox,QMessageBox,QMainWindow
from PyQt6.QtGui import QPixmap
import sys

class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.count = 0
        self.setWindowTitle("My First PyQT Window")
        self.setGeometry(0,0,400,150)


        button = QPushButton("Show Messagebox",self)
        button.setGeometry(150,80,200,40)
        button.clicked.connect(self.show_messagebox)

    def show_messagebox(self):
        msg = QMessageBox()
        msg.setWindowTitle("Message box title")
        msg.setText("This is a simpe QMessageBox")
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
        msg.setDefaultButton(QMessageBox.StandardButton.Ok)
        msg.exec()
        result = msg.exec()
        if result==QMessageBox.StandardButton.Ok:
            print("Ok Button is clicked")
        else:
            print("Cancel Button is clicked")



app = QApplication(sys.argv)
window = Window()
window.show()


sys.exit(app.exec())

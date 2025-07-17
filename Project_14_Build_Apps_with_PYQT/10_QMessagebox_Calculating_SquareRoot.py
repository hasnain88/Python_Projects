from PyQt6.QtWidgets import QWidget,QApplication,QLabel, QPushButton
from PyQt6.QtWidgets import QLineEdit,QCheckBox,QMessageBox,QMainWindow
from PyQt6.QtGui import QPixmap
import sys
import math

class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.count = 0
        self.setWindowTitle("My First PyQT Window")
        self.setGeometry(0,0,400,150)

        number_label = QLabel("Enter a Number: ",self)
        number_label.move(20,20)

        self.number_input = QLineEdit(self)
        self.number_input.move(200,20)

        calculate_button = QPushButton("Find Root",self)
        calculate_button.move(200,60)
        calculate_button.clicked.connect(self.calculate_squareroot)
        
        self.result_label = QLabel("Result ",self)
        self.result_label.move(20,100)

    def calculate_squareroot(self):
        try:
            number = float(self.number_input.text())
            sqaure_root = math.sqrt(number)
            if sqaure_root.is_integer():
                self.result_label.setText("Square root: "+str(sqaure_root))
            else:
                msg = QMessageBox.warning(self,"Not a perfect square", "The number is not a perfect square")
        except ValueError:
            warning = QMessageBox.warning(self,"Invalid input","Please enter a valid number.. ")
                    


        

app = QApplication(sys.argv)
window = Window()
window.show()


sys.exit(app.exec())

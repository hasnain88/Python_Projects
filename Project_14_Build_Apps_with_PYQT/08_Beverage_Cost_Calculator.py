from PyQt6.QtWidgets import QWidget,QApplication,QLabel, QPushButton, QLineEdit,QCheckBox
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

        # Total Cost of Coffee

        self.total_cost = 0
        label = QLabel(self)
        label.setText("Select your options")
        label.resize(200,20)
        label.move(20,20)

        sugar_checkbox = QCheckBox(self)
        sugar_checkbox.setText("Sugar ($ 0.5)")
        sugar_checkbox.move(20,40)
        sugar_checkbox.toggled.connect(self.sugar_checked)
        
        milk_checkbox = QCheckBox(self)
        milk_checkbox.setText("Milk ($ 1.0)")
        milk_checkbox.move(20,60)
        milk_checkbox.toggled.connect(self.milk_checked)

        self.result_label = QLabel(self)
        self.result_label.setText("Total Cost is $0")
        self.result_label.resize(200,20)
        self.result_label.move(20,90)

    def sugar_checked(self,checked):
        if checked:
            self.total_cost += 0.5
        else:
            self.total_cost -= 0.5
        self.result_label.setText("Total Cost :$" + str(self.total_cost))

    def milk_checked(self,checked):
        if checked:
            self.total_cost += 1
        else:
            self.total_cost -= 1
        self.result_label.setText("Total Cost :$" + str(self.total_cost))
  



app = QApplication(sys.argv)
window = Window()
window.show()


sys.exit(app.exec())

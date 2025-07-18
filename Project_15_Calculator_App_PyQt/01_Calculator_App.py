from PyQt6.QtWidgets import QWidget,QApplication,QLabel, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt6.QtWidgets import QLineEdit,QCheckBox,QMessageBox,QMainWindow, QGridLayout
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
import sys
import math

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        
        self.count = 0
        self.setWindowTitle("Calculator")
        
        self.current_input = "0"
        self.previous_input = ""
        self.current_operator = ""

        layout = QGridLayout()
        self.setLayout(layout)

        self.display = QLabel("0")
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        layout.addWidget(self.display,0,0,1,4)

        buttons = [QPushButton(str(i)) for i in range(10)]
        operator = ['+','-','*','/']

        self.equals_buttons = QPushButton("=")
        self.equals_buttons.clicked.connect(self.calculate)
        
        self.clear_buttons = QPushButton("C")
        self.clear_buttons.clicked.connect(self.clear)

        operator_buttons = [QPushButton(op) for op in operator]
        for button in operator_buttons:
            button.clicked.connect(self.operator_button_clicked)

        for i, button in enumerate(buttons):
            row, col = divmod(i,3) # Column span
            layout.addWidget(button,row+1,col)

        # Adding event handling to Method
        for button in buttons: 
            button.clicked.connect(self.number_button_clicked)



        for i, op_button in enumerate(operator_buttons):
            layout.addWidget(op_button,i+1,3)

        layout.addWidget(self.equals_buttons,4,1)
        layout.addWidget(self.clear_buttons,4,2)

    ## Creating a method to handle number button clicked
    def number_button_clicked(self):
        digit = self.sender().text()

        if self.current_input == "0":
            self.current_input=digit
        else:
            self.current_input+=digit
        self.display.setText(self.current_input)
    
    def operator_button_clicked(self):
        operator = self.sender().text()
        if self.current_operator =='':
            self.current_operator= operator
            self.previous_input = self.current_input
            self.current_input = '0'
        else:
            self.calculate()
            self.current_operator= operator
            self.previous_input = self.current_input
            self.current_input = '0'
            
    def calculate(self):
        if self.current_operator=='+':
            result = str(float(self.previous_input) + float(self.current_input))
        elif self.current_operator=='-':
            result = str(float(self.previous_input) - float(self.current_input))
        elif self.current_operator=='*':
            result = str(float(self.previous_input) * float(self.current_input))
        elif self.current_operator=='/':
            if self.current_input=="0":
                result="Error"
            else:
                result = str(float(self.previous_input) / float(self.current_input))
        else:
            result=self.current_input
        
        self.display.setText(result)
        self.current_input = result
        self.current_operator=""

    def clear(self):
        self.current_input = "0"
        self.previous_input = ""
        self.current_operator = ""
        self.display.setText(self.current_input)


app = QApplication(sys.argv)
window = Window()
window.show()


sys.exit(app.exec())

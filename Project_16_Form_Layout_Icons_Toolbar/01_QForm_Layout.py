from PyQt6.QtWidgets import QWidget,QApplication,QLabel, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt6.QtWidgets import QLineEdit,QCheckBox,QMessageBox,QMainWindow, QGridLayout,QFormLayout
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
import sys
import math

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("From Layout")
        self.setGeometry(100,100,400,200,)

        label1 = QLabel("Name")
        name_edit = QLineEdit()

        label2 = QLabel("Age")
        age_edit = QLineEdit()

        form_layout = QFormLayout()
        self.setLayout(form_layout)

        form_layout.addRow(label1,name_edit)
        form_layout.addRow(label2,age_edit)



app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
from PyQt6.QtWidgets import QWidget,QApplication,QLabel, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt6.QtWidgets import QLineEdit,QCheckBox,QMessageBox,QMainWindow, QGridLayout,QFormLayout,QComboBox, QTextEdit
from PyQt6.QtWidgets import QStackedLayout
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
        self.setGeometry(100,100,400,300)

        combo_box = QComboBox()
        combo_box.addItems(['Label','Form'])
        combo_box.activated.connect(self.change_page)

        ## Creating Page 1

        label = QLabel("This is the Label Page")


        ## Creating Page 2
        form = QFormLayout()
        form.addRow("",QLabel("This is a form page"))
        page2_container = QWidget()
        page2_container.setLayout(form)

        ## Creating a stack layout
        self.stacked_layout = QStackedLayout()
        self.stacked_layout.addWidget(label)
        self.stacked_layout.addWidget(page2_container)

        main_layout = QVBoxLayout()
        main_layout.addWidget(combo_box)
        main_layout.addLayout(self.stacked_layout)

        self.setLayout(main_layout)

    def change_page(self,index):
        self.stacked_layout.setCurrentIndex(index)



app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
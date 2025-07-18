from PyQt6.QtWidgets import QWidget,QApplication,QLabel, QPushButton, QHBoxLayout
from PyQt6.QtWidgets import QLineEdit,QCheckBox,QMessageBox,QMainWindow, QGridLayout,QFormLayout
from PyQt6.QtWidgets import QStackedLayout,QVBoxLayout,QComboBox, QTextEdit
from PyQt6.QtGui import QPixmap, QAction
from PyQt6.QtCore import Qt
import sys
import math

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("Manu")
        self.setGeometry(100,100,400,300)

        toolbar = self.addToolBar("Main Toolbar")   


        self.new_action = QAction("New") 
        toolbar.addAction(self.new_action)
        toolbar.addSeparator()
        self.open_action = QAction("Open") 
        toolbar.addAction(self.open_action)
        toolbar.addSeparator()
        self.save_action = QAction("Save") 
        toolbar.addAction(self.save_action)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
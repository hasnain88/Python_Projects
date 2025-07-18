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

        #Step 1: Create a manubar
        manu_bar = self.menuBar()

        
        # Creating the menu items
        file_manu = manu_bar.addMenu("File")
        

        # Creating an Action
        self.new_action = QAction("New")
        
        


        ## Addiding action to the menu
        file_manu.addAction(self.new_action)

        ## Additing a Seperator
        file_manu.addSeparator()
 
        ## Creating another action
        self.exit_action = QAction("Exit")
        self.copy_action = QAction("Copy")
        self.pest_action = QAction("Pest")
        file_manu.addAction(self.exit_action)
        file_manu.addAction(self.copy_action)
        file_manu.addAction(self.pest_action)

        # Creating a ner menu        
        edit_manu = manu_bar.addMenu("Edit")
        edit_manu.addAction(self.exit_action)
        edit_manu.addSeparator()
        self.copy_action = QAction("Copy")
        edit_manu.addAction(self.copy_action)
        edit_manu.addSeparator()
        self.pest_action = QAction("Pest")       
        edit_manu.addAction(self.pest_action)

        


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
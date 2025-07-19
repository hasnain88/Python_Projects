from PyQt6.QtWidgets import QWidget,QApplication,QLabel, QPushButton, QHBoxLayout
from PyQt6.QtWidgets import QLineEdit,QCheckBox,QMessageBox,QMainWindow, QGridLayout,QFormLayout
from PyQt6.QtWidgets import QStackedLayout,QVBoxLayout,QComboBox, QTextEdit,QToolBar
from PyQt6.QtGui import QPixmap, QAction,QIcon
from PyQt6.QtCore import Qt
import sys
import math
import os

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("Manu")
        self.setGeometry(100,100,400,300)

        # Path to icons folder
        self.icon_dir = os.path.join(os.path.dirname(__file__), "icons")

        # Create a toolbar
        toolbar = QToolBar("Main Toolbar")
        self.addToolBar(toolbar)

        # Add actions with icons
        self.add_action(toolbar, "New", "new.png")
        self.add_action(toolbar, "Open", "open.png")
        self.add_action(toolbar, "Save", "save.png")
        self.add_action(toolbar, "Exit", "exit.png", self.close)

    def add_action(self, toolbar, name, icon_file, callback=None):
        icon_path = os.path.join(self.icon_dir, icon_file)
        action = QAction(QIcon(icon_path), name, self)
        if callback:
            action.triggered.connect(callback)
        toolbar.addAction(action)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
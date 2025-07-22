from PyQt6.QtWidgets import QWidget,QApplication,QLabel, QPushButton, QLineEdit,QStyleFactory,QVBoxLayout
from PyQt6.QtWidgets import QGroupBox, QHBoxLayout,QTabWidget, QRadioButton, QCheckBox,QMainWindow
from PyQt6.QtGui import QPixmap
import sys

from todolist import Ui_Form



class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        self.initUI()

    
    def initUI(self):
        self.setGeometry(0,0,400,300)
        self.ui.addTaskButton.clicked.connect(self.add_task)
        self.ui.deleteButton.clicked.connect(self.delete_task)
    
        
    
    def add_task(self):
        task = self.ui.taskEdit.text()
        if task:
            self.ui.taskList.addItem(task)
            self.ui.taskEdit.clear()

    def delete_task(self):
        selected_task = self.ui.taskList.currentItem()
        if selected_task:
            self.ui.taskList.takeItem(self.ui.taskList.row(selected_task))
            
    
        
app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())

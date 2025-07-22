from PyQt6.QtWidgets import QWidget,QApplication,QLabel, QPushButton, QLineEdit,QStyleFactory,QVBoxLayout
from PyQt6.QtWidgets import QGroupBox, QHBoxLayout,QTabWidget, QRadioButton, QCheckBox,QMainWindow
from PyQt6.QtGui import QPixmap
import sys
from demo_QT_GUI import Ui_Form



class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.initUI()

    
    def initUI(self):
        self.setGeometry(0,0,400,300)
        self.ui.lineEdit.setMaxLength(8)
        self.ui.lineEdit_2.setMaxLength(8)

        self.ui.pushButton.clicked.connect(self.check)

    def check(self):
        username = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()

        if username=='admin' and password=="admin123":
            print("Valid Username and Password")
        else:
            print("Invalid Username and Password")

        
    
        
app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())

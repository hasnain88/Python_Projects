from PyQt6.QtWidgets import QWidget,QApplication,QLabel, QPushButton, QLineEdit,QStyleFactory,QVBoxLayout
from PyQt6.QtWidgets import QGroupBox, QHBoxLayout,QTabWidget
from PyQt6.QtGui import QPixmap
import sys



class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0,0,700,150)


        # Creating a tab widget
        tab_widget = QTabWidget()

        # Create tabs
        tab1 = QTabWidget()
        tab2 = QTabWidget()

        # Additing above tabs to tab widget
        tab_widget.addTab(tab1,'Tab 1')
        tab_widget.addTab(tab2,'Tab 2')

        # Create widget to be added to tabs
        button1=QPushButton('Submit1')
        button2=QPushButton('Submit2')

        

        layout1 = QVBoxLayout()       
        layout1.addWidget(button1)

        layout2 = QVBoxLayout()       
        layout2.addWidget(button2)

        
        # Setting the tab layout to layout 1 and layout 2
        tab1.setLayout(layout1)
        tab2.setLayout(layout2)

        # Add the tab widget to tha main window
        layout = QVBoxLayout(self)
        layout.addWidget(tab_widget)
        
app = QApplication(sys.argv)

window = Window()
window.show()
sys.exit(app.exec())

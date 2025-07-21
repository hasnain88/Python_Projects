from PyQt6.QtWidgets import QWidget,QApplication,QLabel, QPushButton, QLineEdit,QStyleFactory,QVBoxLayout
from PyQt6.QtWidgets import QGroupBox
from PyQt6.QtGui import QPixmap
import sys



class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0,0,700,150)
        # Step 1 Creating a container
        box = QGroupBox()

        # Step 2 Creating widgets to be added to the container
        button1 = QPushButton("Button 1")
        button2 = QPushButton("Button 2")
               
        # Step 3 Create a layout and add the above widgets
        layout = QVBoxLayout()
        layout.addWidget(button1)
        layout.addWidget(button2)

        # Step 4 Add the above layout to container
        box.setLayout(layout)

        # Step 5 Set the main window's layout to the container
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(box)

        



app = QApplication(sys.argv)

window = Window()
window.show()
sys.exit(app.exec())

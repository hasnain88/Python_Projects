from PyQt6.QtWidgets import QWidget,QApplication,QLabel, QPushButton, QLineEdit,QStyleFactory,QVBoxLayout
from PyQt6.QtWidgets import QGroupBox, QHBoxLayout,QTabWidget, QRadioButton, QCheckBox
from PyQt6.QtGui import QPixmap
import sys



class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0,0,700,150)

        tab_widget = QTabWidget()


        tea_tab = QWidget()
        coffee_tab = QWidget()

        tab_widget.addTab(tea_tab,"Tea")
        tab_widget.addTab(coffee_tab,"Coffee")

        # Tea Layout
        tea_layout = QVBoxLayout()
        liquid_label = QLabel("Select Milk / Water")
        milk_button = QRadioButton("Milk")
        water_button = QRadioButton("Water")

        # Create container for milk/water
        liquid_group = QGroupBox()

        #Creating a layout for liquid container
        liquid_group_layout = QVBoxLayout()
        liquid_group_layout.addWidget(milk_button)
        liquid_group_layout.addWidget(water_button)
        liquid_group.setLayout(liquid_group_layout)
        tea_layout.addWidget(liquid_label)
        tea_layout.addWidget(liquid_group)


        
        spice_box_label = QLabel("Select Spice Layout")
        tea_layout.addWidget(spice_box_label)

        #Creating spice container
        spice_box = QGroupBox()
        #Creating layout for spice box
        spice_box_layout = QVBoxLayout()
        spice_box.setLayout(spice_box_layout)

        spices = ['Sugar','Clove', 'Black Paper','Cinamon','Tumrmuric']
        for spice in spices:
            spice_check_box = QCheckBox(spice)
            spice_box_layout.addWidget(spice_check_box)

        tea_layout.addWidget(spice_box)
        # Creating a layout for Liquid container

        tea_tab.setLayout(tea_layout)
       
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(tab_widget)
    
        
app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())

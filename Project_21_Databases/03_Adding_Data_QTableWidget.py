from PyQt6.QtWidgets import QWidget,QApplication,QLabel, QPushButton, QLineEdit,QListWidget,QListWidgetItem,QHBoxLayout,QTableWidget,QMainWindow,QTableWidgetItem
from PyQt6.QtGui import QPixmap
import sys

class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        
        self.setWindowTitle("Databases")
        self.setGeometry(0,0,400,150)

        people = [
            {'First Name':'John', 'Last Name':'Doe','Age':21},
            {'First Name':'Rob', 'Last Name':'Ford','Age':31},
            {'First Name':'Bob', 'Last Name':'Doe','Age':41},
            ]

        self.table_widget = QTableWidget()
        self.setCentralWidget(self.table_widget)
        self.table_widget.setRowCount(len(people))
        self.table_widget.setColumnCount(3)
        self.table_widget.setHorizontalHeaderLabels(people[0].keys())

        row = 0
        for person in people:
            self.table_widget.setItem(row,0,QTableWidgetItem(person['First Name']))
            self.table_widget.setItem(row,1,QTableWidgetItem(person['Last Name']))
            self.table_widget.setItem(row,2,QTableWidgetItem(str(person['Age'])))
            row+=1

app = QApplication(sys.argv)
window = Window()
window.show()


sys.exit(app.exec())

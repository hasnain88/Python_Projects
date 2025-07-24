from PyQt6.QtWidgets import QWidget,QApplication,QLabel, QPushButton, QLineEdit,QListWidget,QListWidgetItem,QHBoxLayout,QTableWidget,QMainWindow
from PyQt6.QtGui import QPixmap
import sys

class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.count = 0
        self.setWindowTitle("Databases")
        self.setGeometry(0,0,400,150)

        self.table_widget = QTableWidget()
        self.setCentralWidget(self.table_widget)
        self.table_widget.setRowCount(10)
        self.table_widget.setColumnCount(10)






app = QApplication(sys.argv)
window = Window()
window.show()


sys.exit(app.exec())

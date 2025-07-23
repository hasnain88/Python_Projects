from PyQt6.QtWidgets import QMainWindow, QApplication,QLabel
from PyQt6.QtGui import QPixmap, QColor,QPainter,QPen
from PyQt6.QtCore import Qt,QPoint

import sys 

class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.iniUI()
               
    
    def iniUI(self):
        self.setMinimumSize(400,400)
        self.setWindowTitle("Paint App")

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        pen = QPen(QColor('#ebe124'),5,)
        painter.setPen(pen)
        painter.drawPoint(100,100)
        painter.drawLine(0,0,100,100)
        painter.drawRect(100,100,200,200)
        painter.drawEllipse(100,100,200,200)
        
        painter.end()


     
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
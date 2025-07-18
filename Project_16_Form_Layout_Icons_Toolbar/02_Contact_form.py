from PyQt6.QtWidgets import QWidget,QApplication,QLabel, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt6.QtWidgets import QLineEdit,QCheckBox,QMessageBox,QMainWindow, QGridLayout,QFormLayout,QComboBox, QTextEdit
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
import sys
import math

class Window(QWidget):
    def __init__(self):
        super().__init__()
        
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("From Layout")
        self.setGeometry(100,100,400,300)

        form_layout = QFormLayout(self)
        self.setLayout(form_layout)

        self.name_edit = QLineEdit()
        self.email_edit = QLineEdit()
        self.phone_edit = QLineEdit()
        self.subject_combo = QComboBox()
        self.subject_combo.addItems(['Select Subject',"Personal","Business"])
        self.message_edit = QTextEdit()
        submit_button = QPushButton("Submit")
        submit_button.clicked.connect(self.submitClicked)

        
        form_layout.addRow(QLabel("Name"),self.name_edit)
        form_layout.addRow(QLabel("Email"),self.email_edit)
        form_layout.addRow(QLabel("Phone Number"),self.subject_combo)
        form_layout.addRow(QLabel("Subject"),self.phone_edit)
        form_layout.addRow(QLabel("Message"),self.message_edit)
        form_layout.addRow(submit_button)

    def submitClicked(self):
        name = self.name_edit.text()
        email = self.name_edit.text()
        phone = self.phone_edit.text()
        subject = self.subject_combo.currentText()
        message = self.message_edit.toPlainText()

        print(f"Name: {name} \n Email: {email} \n phone: {phone} \n Subject {subject} \n Message {message}\n ")


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
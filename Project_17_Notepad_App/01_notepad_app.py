from PyQt6.QtWidgets import QWidget,QApplication,QLabel, QPushButton, QHBoxLayout
from PyQt6.QtWidgets import QLineEdit,QCheckBox,QMessageBox,QMainWindow, QGridLayout,QFormLayout
from PyQt6.QtWidgets import QStackedLayout,QVBoxLayout,QComboBox, QTextEdit, QMenuBar, QMenu
from PyQt6.QtWidgets import QFileDialog, QInputDialog
from PyQt6.QtGui import QPixmap, QAction,QIcon,QTextCursor,QColor
from PyQt6.QtCore import Qt
import sys
import math
import os

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("Notepad")
        self.setGeometry(100,100,400,300)

        self.current_file = None

        self.edit_field = QTextEdit(self)
        self.setCentralWidget(self.edit_field)



        # Create a menubar
        menubar = QMenuBar(self)
        self.setMenuBar(menubar)

        # Creating Manu
        filemanu = QMenu("File",self)
        menubar.addMenu(filemanu)

        # Creating Edit Menu
        editmanu = QMenu("edit",self)
        menubar.addMenu(editmanu)


        # Creating actions for File Manue
        new_action = QAction("New",self)
        filemanu.addAction(new_action)
        new_action.triggered.connect(self.new_file)

        open_action = QAction("Open",self)
        filemanu.addAction(open_action)
        open_action.triggered.connect(self.open_file)

        save_action = QAction("Save",self)
        filemanu.addAction(save_action)
        save_action.triggered.connect(self.save_file)

        save_as_action = QAction("Save As",self)
        filemanu.addAction(save_as_action)
        save_as_action.triggered.connect(self.save_as_file)

        # Creating actions for Edit Manu

        undo_action = QAction("Undo",self)
        editmanu.addAction(undo_action)
        undo_action.triggered.connect(self.edit_field.undo)

        redo_action = QAction("Redo",self)
        editmanu.addAction(redo_action)
        redo_action.triggered.connect(self.edit_field.redo)

        cut_action = QAction("Cut",self)
        editmanu.addAction(cut_action)
        cut_action.triggered.connect(self.edit_field.cut)

        paste_action = QAction("Paste",self)
        editmanu.addAction(paste_action)
        paste_action.triggered.connect(self.edit_field.paste)

        copy_action = QAction("Copy",self)
        editmanu.addAction(copy_action)
        copy_action.triggered.connect(self.edit_field.copy)

        find_action = QAction("Find",self)
        editmanu.addAction(find_action)
        find_action.triggered.connect(self.find_text)
        



    def new_file(self):
        self.edit_field.clear()
        self.current_file=None  


    def open_file(self):
        print("Opening the File")
        file_path,_ = QFileDialog.getOpenFileName(self,"Open File","","All Files(*);; Python File (*.py)")
        if file_path:
            with open(file_path,"r") as file:
                text = file.read()
                self.edit_field.setText(text)
            

    def save_file(self):
        if self.current_file:
            with open(self.current_file,"w") as file:
                file.write(self.edit_field.toPlainText())
        else:
            self.save_as_file()


    
    def save_as_file(self):
        print("Saving the File AS")
        file_path,_ = QFileDialog.getSaveFileName(self,"Save File","","All Files(*);; Python File(*.py)")
        if file_path:
            with open(file_path,"w") as file:
                file.write(self.edit_field.toPlainText())
            self.current_file = file_path
    
    def find_text(self):
        print("Finding text")
        search_text,ok = QInputDialog.getText(self,"Find Text","Search for ")
        if ok:
            all_words =[]
            self.edit_field.moveCursor(QTextCursor.MoveOperation.Start)
            highlight_color = QColor(Qt.GlobalColor.yellow)

            while(self.edit_field.find(search_text)):
                selection = QTextEdit.ExtraSelection()
                selection.format.setBackground(highlight_color)
                selection.cursor = self.edit_field.textCursor()
                all_words.append(selection)
            self.edit_field.setExtraSelections(all_words)
            
        

            

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
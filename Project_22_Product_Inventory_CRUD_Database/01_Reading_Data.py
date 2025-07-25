from PyQt6.QtWidgets import QWidget,QApplication,QLabel, QPushButton, QLineEdit,QListWidget,QListWidgetItem,QHBoxLayout,QTableWidget,QMainWindow,QTableWidgetItem
from PyQt6.QtWidgets import QDockWidget, QFormLayout, QLineEdit,QSpinBox, QToolBar, QMessageBox,QMenu,QVBoxLayout
from PyQt6.QtGui import QPixmap, QAction, QIcon
from PyQt6.QtCore import Qt,QSize
import sys
import os


# CRUD Cread, Read, Update, Delete

class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.products = [
            {'name':'iPhone','price':500,'description':'This is an iPhone'},
            {'name':'iPad','price':1500,'description':'This is an iPad'},
            {'name':'iMax','price':2500,'description':'This is an iMax'},
            ] 
        self.initUI()

    def initUI(self):
        self.setWindowTitle("CURD APP")
        self.setGeometry(0,0,400,150)

        central_widget = QTableWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        self.table_widget = QTableWidget(self)
        layout.addWidget(self.table_widget)

        self.table_widget.setRowCount(len(self.products))
        self.table_widget.setColumnCount(len(self.products[0]))

        # self.table_widget.setHorizontalHeaderLabels(self.products[0].keys())
        self.table_widget.setHorizontalHeaderLabels(['Name','Price','Description'])
        
        for row, product in enumerate(self.products):
            for col,value in enumerate(product.values()):
                item = QTableWidgetItem(str(value))
                self.table_widget.setItem(row,col,item)
        
        self.name_edit = QLineEdit(self)
        self.price_edit = QLineEdit(self)
        self.description_edit = QLineEdit(self)

        layout.addWidget(QLabel("Name:"))
        layout.addWidget(self.name_edit)

        layout.addWidget(QLabel("Price:"))
        layout.addWidget(self.price_edit)

        layout.addWidget(QLabel("Description:"))
        layout.addWidget(self.description_edit)


        add_button = QPushButton("Add Products",self)
        add_button.clicked.connect(self.add_product)
        

        delete_button = QPushButton("Delete Product",self)
        delete_button.clicked.connect(self.delete_product)

        update_button = QPushButton("Update Product",self)
        update_button.clicked.connect(self.update_button)

        layout.addWidget(add_button)
        layout.addWidget(delete_button)
        layout.addWidget(update_button)
    
    def delete_product(self):
        current_row = self.table_widget.currentRow()
        if current_row < 0 or current_row >=self.table_widget.rowCount():
            return QMessageBox.warning(self,"No Row Selected")
        
        button = QMessageBox.question(self,"Delete Product","Do you want to delete product???",QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if button == QMessageBox.StandardButton.Yes:
            self.table_widget.removeRow(current_row)
            del self.products[current_row]

    def update_button(self):
        current_row = self.table_widget.currentRow()
        if current_row < 0 or current_row >=self.table_widget.rowCount():
            return QMessageBox.warning(self,"No Row Selected")
        
        name = self.name_edit.text().strip()
        price = self.price_edit.text().strip()
        description = self.description_edit.text().strip()

        updated_product = {'name':name,'price':price,'description':description}
        self.products[current_row]=updated_product

        for col, value in enumerate(updated_product.values()):
            item = QTableWidgetItem(str(value))
            self.table_widget.setItem(current_row,col,item)
        


    
    def add_product(self):
        name = self.name_edit.text().strip()
        price = self.price_edit.text().strip()
        description = self.description_edit.text().strip()

        new_product = {'name':name,'price':price,'description':description}
        self.products.append(new_product)

        # Updating the table
        row_position = len(self.products)-1
        self.table_widget.insertRow(row_position)

        for col, value in enumerate(new_product.values()):
            item = QTableWidgetItem(str(value))
            self.table_widget.setItem(row_position,col,item)
        
        self.name_edit.clear()
        self.price_edit.clear()
        self.description_edit.clear()

    


        

                     

       



app = QApplication(sys.argv)
window = Window()
window.show()


sys.exit(app.exec())

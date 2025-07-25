from PyQt6.QtWidgets import QWidget,QApplication,QLabel, QPushButton, QLineEdit,QListWidget,QListWidgetItem,QHBoxLayout,QTableWidget,QMainWindow,QTableWidgetItem
from PyQt6.QtWidgets import QDockWidget, QFormLayout, QLineEdit,QSpinBox, QToolBar, QMessageBox,QMenu,QVBoxLayout
from PyQt6.QtGui import QPixmap, QAction, QIcon
from PyQt6.QtCore import Qt,QSize
import sys
import os
import sqlite3

# CRUD Cread, Read, Update, Delete

class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        
        self.conn = sqlite3.connect('products.db')
        self.create_table()
        self.initUI()
    
    
    def load_data(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM products")
        products = cursor.fetchall()
        self.table_widget.setRowCount(len(products))
        for row, product in enumerate(products):
            for col,value in enumerate(product):
                item = QTableWidgetItem(str(value))
                self.table_widget.setItem(row,col,item)
        

    def create_table(self):
    
        cursor = self.conn.cursor()
        cursor.execute("""
                CREATE TABLE IF NOT EXISTS products (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       name TEXT,
                       price INTEGER,
                       description TEXT
                       )
                
                """)
        self.conn.commit()

    def initUI(self):
        self.setWindowTitle("CURD APP")
        self.setGeometry(0,0,400,150)
        # self.load_data()

        central_widget = QTableWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        self.table_widget = QTableWidget(self)
        layout.addWidget(self.table_widget)

        # self.table_widget.setRowCount(4)
        self.table_widget.setColumnCount(4)

        # self.table_widget.setHorizontalHeaderLabels(self.products[0].keys())
        self.table_widget.setHorizontalHeaderLabels(['ID','Name','Price','Description'])
        self.load_data()

        
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
        product_id = int(self.table_widget.item(current_row,0).text())
        button = QMessageBox.question(self,"Delete Product","Do you want to delete product???",QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if button == QMessageBox.StandardButton.Yes:
            cursor = self.conn.cursor()
            cursor.execute("DELETE FROM products WHERE id=?",(product_id,))
            self.conn.commit()  
            self.load_data()   

    def update_button(self):
        current_row = self.table_widget.currentRow()
        if current_row < 0 or current_row >=self.table_widget.rowCount():
            return QMessageBox.warning(self,"No Row Selected")
        
        name = self.name_edit.text().strip()
        price = self.price_edit.text().strip()
        description = self.description_edit.text().strip()
        product_id = int(self.table_widget.item(current_row,0).text())
        cursor = self.conn.cursor()
        cursor.execute("UPDATE products SET name=?, price=?, description=? WHERE iD=?",(name,price,description,product_id))
        self.conn.commit()  
        self.load_data()


        

        


    
    def add_product(self):
        name = self.name_edit.text().strip()
        price = self.price_edit.text().strip()
        description = self.description_edit.text().strip()
        
        ## Adding new product to the database
        cursor = self.conn.cursor()
        cursor.execute("""
                    INSERT INTO  products (name,price,description) VALUES (?,?,?)
                """,(name,price,description))
        self.conn.commit()  
        self.load_data()      
        self.name_edit.clear()
        self.price_edit.clear()
        self.description_edit.clear()

    


        

                     

       



app = QApplication(sys.argv)
window = Window()
window.show()


sys.exit(app.exec())

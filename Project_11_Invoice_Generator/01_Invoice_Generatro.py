from tkinter import *

medicines = {
    "Medicine A":10,
    "Medicine B":20,
    "Medicine C":30,
    "Medicine D":40,
    "Medicine E":70,
    "Medicine G":50,
    "Medicine H":10,
    "Medicine I":20,
    "Medicine J":30,
    "Medicine K":40,
    "Medicine L":70,
    "Medicine M":50,

}

def add_medicine():
    pass

window = Tk()
window.title("Invoice Generator")

medicine_lable = Label(window, text="Medicine: ")
medicine_lable.pack()

medicine_listbox = Listbox(window,selectmode=SINGLE)
for medicine in medicines:
    medicine_listbox.insert(END,medicine)

medicine_listbox.pack()

quantity_label = Label(window, text="Quantity")
quantity_label.pack()
quantity_entry = Entry(window)
quantity_entry.pack()

add_button = Button(window,text="Add Medicine",command=add_medicine)
add_button.pack()

total_amount_label = Label(window, text="Total Amount")
total_amount_label.pack()
total_amount_entry = Entry(window)
total_amount_entry.pack()


customer_label = Label(window, text="Customer Name")
customer_label.pack()
customer_entry = Entry(window)
customer_entry.pack()


generate_button = Button(window, text="Generate Invoice")
generate_button.pack()

invoice_text = Text(window,height=10, width=50)
invoice_text.pack()

window.mainloop()
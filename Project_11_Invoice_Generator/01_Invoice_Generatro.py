from tkinter import *
from fpdf import FPDF



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


invoice_items=[]


def add_medicine():
    selected_medicine = medicine_listbox.get(ANCHOR)
    quantity = int(quantity_entry.get())
    price = medicines[selected_medicine]
    item_total = price * quantity
    invoice_items.append((selected_medicine,quantity,item_total))
    total_amount_entry.delete(0,END)
    total_amount_entry.insert(END,str(calculate_total()))
    update_invoice_text()
    


def calculate_total():
    total = 0.0
    for item in invoice_items:
        total+=item[2]
    return total




def update_invoice_text():
    invoice_text.delete(1.0,END)
    for item in invoice_items:
        invoice_text.insert(END,f"Medicine: {item[0]}, Quantity: {item[1]}, Total: {item[2]}\n")


def generate_invoice():
    customer_name = customer_entry.get()

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("helvetica",size=12)
    pdf.cell(0,10, text="Invoice", new_x="LMARGIN", new_y="NEXT",align="C")    
    pdf.cell(0,10, text="Customer: "+customer_name, new_x="LMARGIN", new_y="NEXT",align="L")
    pdf.cell(0,10, text="", new_x="LMARGIN", new_y="NEXT")
    for item in invoice_items:
        medicine_name, quantity, item_total = item
        pdf.cell(0,10, text=f"Medicine: {medicine_name}, Quantity: {quantity}, Total: {item_total}",
                  new_x="LMARGIN", new_y="NEXT", align="L")
    pdf.cell(0,10, text="Total Amount: "+str(calculate_total()),new_x="LMARGIN", new_y="NEXT",align='L')
    pdf.output("invoice.pdf")




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


generate_button = Button(window, text="Generate Invoice",command=generate_invoice)
generate_button.pack()

invoice_text = Text(window,height=10, width=50)
invoice_text.pack()

window.mainloop()
from tkinter import *
import pyqrcode
from PIL import ImageTk, Image
import os

def generate():
    link_name = name_entry.get().strip()
    link = link_entry.get().strip()

    if not link_name or not link:
        status_label.config(text="❌ Please enter both name and link.", fg="red")
        return

    file_name = link_name + ".png"
    
    try:
        # Generate and save QR code
        url = pyqrcode.create(link)
        url.png(file_name, scale=8)

        # Open and resize image using correct resampling
        image = Image.open(file_name)
        image = image.resize((200, 200), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        # Show QR code in label
        image_label.config(image=photo)
        image_label.image = photo

        status_label.config(text="✅ QR Code generated successfully!", fg="green")

    except Exception as e:
        status_label.config(text=f"❌ Error: {str(e)}", fg="red")


# Setup window
root = Tk()
root.title("QR Code Generator")
root.geometry("400x600")
root.resizable(False, False)

canvas = Canvas(root, width=400, height=600)
canvas.pack()

# Title Label
app_label = Label(root, text='QR Code Generator', fg='blue', font=("Arial", 24))
canvas.create_window(200, 50, window=app_label)

# Input Labels
name_label = Label(root, text='Link Name')
link_label = Label(root, text='Link (URL)')
canvas.create_window(200, 100, window=name_label)
canvas.create_window(200, 160, window=link_label)

# Entry Fields
name_entry = Entry(root, width=30)
link_entry = Entry(root, width=30)
canvas.create_window(200, 130, window=name_entry)
canvas.create_window(200, 190, window=link_entry)

# Generate Button
button = Button(root, text="Generate QR Code", command=generate)
canvas.create_window(200, 230, window=button)

# Status Label
status_label = Label(root, text="", font=("Arial", 10))
canvas.create_window(200, 270, window=status_label)

# Image display Label
image_label = Label(root)
canvas.create_window(200, 450, window=image_label)

# Run GUI
root.mainloop()

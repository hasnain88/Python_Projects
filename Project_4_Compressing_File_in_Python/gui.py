import tkinter as tk

from compressedmodule import compress,decompress
from tkinter import filedialog

def compression(i,o):
    compress(i,o)

def decompression(i,o):
    decompress(i,o)

window = tk.Tk()
window.title("File Compressor/Decompressor")
window.geometry('600x400')



input_entry = tk.Entry(window)
output_entry = tk.Entry(window)

input_label = tk.Label(window,text="File to be compressed / or Decompressed")
input_label.grid(row=0,column=0)

outpu_label = tk.Label(window,text="Name of the compressed file")
outpu_label.grid(row=1,column=0)

input_entry.grid(row=0,column=1)
output_entry.grid(row=1,column=1)

compress_button = tk.Button(window,text="Compress",command=lambda: compression(input_entry.get(), output_entry.get()))
compress_button.grid(row=2,column=0)
decompress_button = tk.Button(window,text="Decompress",command=lambda: decompress(input_entry.get(), output_entry.get()))
decompress_button.grid(row=2,column=1)

window.mainloop()
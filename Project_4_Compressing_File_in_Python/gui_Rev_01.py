import tkinter as tk
import os
import zlib,base64

# from compressedmodule import compress,decompress
from tkinter import filedialog

def open_file():
    filename = filedialog.askopenfilename(initialdir='/',title="Select a file for Compress")
    return filename

# def compression(i,o):
#     compress(i,o)

# def decompression(i,o):
#     decompress(i,o)

def compress(inputfile, outputfile):
    data = open(inputfile,'r').read()
    data_bytes = bytes(data,'utf-8')
    compressed_data = base64.b64encode(zlib.compress(data_bytes,9))
    decoded_data = compressed_data.decode('utf-8')
    compressed_file = open(outputfile,'w')
    compressed_file.write(decoded_data)

# compress('demo.txt','ot.txt')

def decompress(inputfile, outputfile):
    file_content  = open(inputfile,'r').read()
    encoded_data = file_content.encode('utf-8')
    decompressed_data = zlib.decompress(base64.b64decode(encoded_data))
    decoded_data = decompressed_data.decode('utf-8')
    file = open(outputfile,'w')
    file.write(decoded_data)
    file.close



window = tk.Tk()
window.title("File Compressor/Decompressor")
window.geometry('600x400')


compress_button = tk.Button(window,text="Compress",command=lambda: compress(open_file(), "Compressed.txt"))
compress_button.grid(row=2,column=0)

decompress_button = tk.Button(window,text="Decompress",command=lambda: decompress(open_file(), "Decompressed.txt"))
decompress_button.grid(row=2,column=1)

window.mainloop()
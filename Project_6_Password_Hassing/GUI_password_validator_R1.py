import bcrypt
from tkinter import *


def validate(password):
    hash = b'$2b$12$0xa52E3wvRUZy.n/Oi/Rme4B3sVSuiRTC76vp59Y6W.fCVHPKKxUm'
    password = bytes(password, encoding='utf-8')
    if bcrypt.checkpw(password, hash):
        print("Login Sucessful")
    else:
        print("Invalid Password")


root = Tk()
root.geometry("300x300")

password_entry = Entry(root)
password_entry.pack()

button = Button(root, text='validate',command=lambda: validate(password_entry.get()))

button.pack()



root.mainloop()
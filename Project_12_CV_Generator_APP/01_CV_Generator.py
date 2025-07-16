from tkinter import *
from tkinter import messagebox
from fpdf import FPDF
import pyqrcode
from PIL import ImageTk, Image
import os

class PDFCV(FPDF):
    def header(self):
        self.image('mywebsite.png',10,8,33,title='Portfolio Site')

    def footer(self):
        return super().footer()

    def generate_cv(self,name,email,phone, address,skills,work_experiance, education, about_me):
        self.add_page()
        self.ln(20)

        # Displaying Name
        self.set_font('helvetica','B',26)
        self.cell(0,10, name, new_x="LMARGIN",new_y="NEXT",align='C')

        ## Adding contact information
        self.set_font('helvetica','B',12)
        self.cell(0,10, "Contact Information", new_x="LMARGIN",new_y="NEXT",align='L')
       
        self.set_font('helvetica','B',10)
        self.cell(0,5, "Email:{}".format(email), new_x="LMARGIN",new_y="NEXT")
        self.cell(0,5, "Phone:{}".format(phone), new_x="LMARGIN",new_y="NEXT")
        self.cell(0,5, "Email:{}".format(address), new_x="LMARGIN",new_y="NEXT")

        ## Adding Skills
        self.ln(10)
        self.set_font('helvetica','B',12)
        self.cell(0,10, "Skills", new_x="LMARGIN",new_y="NEXT",align='L')

        self.set_font('helvetica','B',10)
        for skill in skills:
            self.cell(0,5,"- {}".format(skill),new_x="LMARGIN",new_y="NEXT")


        ## Additng Work Experiance 
        self.ln(10)
        self.set_font('helvetica','B',12)
        self.cell(0,10, "Work Experiance", new_x="LMARGIN",new_y="NEXT",align='L')

        self.set_font('helvetica','B',10)
        for experinace in work_experiance:
            self.cell(0,5,"{}:{}".format(experinace['title'],experinace['description']),new_x="LMARGIN",new_y="NEXT")


        ## Additng Education
        self.ln(10)
        self.set_font('helvetica','B',12)
        self.cell(0,10, "Education Item", new_x="LMARGIN",new_y="NEXT",align='L')

        self.set_font('helvetica','B',10)
        for edu in education:
            self.cell(0,5,"{}:{}".format(edu['degree'],edu['university']),new_x="LMARGIN",new_y="NEXT")

        ## About Me
        self.ln(10)
        self.set_font('helvetica','B',12)
        self.cell(0,10, "About Me", new_x="LMARGIN",new_y="NEXT",align='L')

        self.set_font('helvetica','B',10)
        self.multi_cell(0,5,about_me)
        

        self.output("cv1.pdf")

        

def generate_cv_pdf():
    name = entry_name.get()
    email = entry_email.get()
    phone = entry_phone.get()
    address = entry_address.get()
    website = entry_website.get()
    skills = entry_skills.get("1.0",END).strip().split('\n')
    work_experiance = []
    education = []

    work_experiance_lines = entry_experiance.get("1.0",END).strip().split('\n')
    for line in work_experiance_lines:
        title, description = line.split(":")
        work_experiance.append({'title':title.strip(), 'description':description.strip()})

    education_lines = entry_education.get("1.0",END).strip().split('\n')
    for line in education_lines:
        degree, university =  line.split(":")
        education.append({'degree':degree.strip(), 'university':university.strip()})

    about_me = entry_about_me.get("1.0",END)

    ## Create QR code 
    qrcode = pyqrcode.create(website)
    qrcode.png("mywebsite.png",scale=6)

    if not name or not email or not phone or not address or not skills or not education or not work_experiance or not about_me:
        messagebox.showerror("Error","Please fill in all the details")
        return

    CV = PDFCV()
    CV.generate_cv(name,email,phone, address,skills,work_experiance, education, about_me)


    

window = Tk()
window.title("CV Generator")

label_name = Label(window, text="Name: ")
label_name.pack()
entry_name = Entry(window)
entry_name.pack()


label_email = Label(window, text="Email: ")
label_email.pack()
entry_email = Entry(window)
entry_email.pack()


label_phone = Label(window, text="Phone: ")
label_phone.pack()
entry_phone = Entry(window)
entry_phone.pack()


label_address = Label(window, text="Address: ")
label_address.pack()
entry_address = Entry(window)
entry_address.pack()


label_website = Label(window, text="Website: ")
label_website.pack()
entry_website = Entry(window)
entry_website.pack()


label_skills = Label(window, text="Skills (Enter one skill one line)")
label_skills.pack()
entry_skills = Text(window,height=5)
entry_skills.pack()

label_education = Label(window, text="Education (One per line in format 'Degree':'University')")
label_education.pack()
entry_education = Text(window,height=5)
entry_education.pack()

label_experiance = Label(window, text="Experiance (One per line in format 'Job Title':'Description')")
label_experiance.pack()
entry_experiance = Text(window,height=5)
entry_experiance.pack()

label_about_me = Label(window, text="About Me")
label_about_me.pack()
entry_about_me = Text(window,height=5)
entry_about_me.pack()


button_generate = Button(window,text="Generate CV",command=generate_cv_pdf)
button_generate.pack()

window.mainloop()
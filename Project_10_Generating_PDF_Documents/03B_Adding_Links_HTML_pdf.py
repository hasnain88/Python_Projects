from fpdf import FPDF




pdf = FPDF()
pdf.add_page()
pdf.set_font("helvetica",size=20)
pdf.write(5,"To find out whats new in tutorial, click")
pdf.set_font(style="U")
link = pdf.add_link(page=2)
pdf.write(5,"here",link)

## Secound Page
pdf.add_page()
pdf.image("Logo.png",10,10,50,0,"","http://www.google.com")
pdf.set_left_margin(60)
pdf.set_font_size(18)
pdf.write_html("<b>This is some bold text</b>")
pdf.write_html(""" You can add any html code in here <b>this bold text </b><h1>This is a heading</h1>
               <a href="http://www.google.com"> click hear to got to google  """)
pdf.output("link.pdf")

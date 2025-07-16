from fpdf import FPDF
import csv

with open("countries.txt",encoding="utf8") as csv_file:
    data = list(csv.reader(csv_file,delimiter=','))

pdf = FPDF()
pdf.set_font("helvetica","B",14)

pdf.add_page()
with pdf.table() as table:
    for data_row in data:
        row = table.row()
        for datum in data_row:
            row.cell(datum)

pdf.output("table.pdf")
# PDF Resume Creator
# 	- Create a python program that will create your personal resume in PDF format
# 	- All personal details are stored in a JSON file
# 	- Your program should read the JSON file and write the details in the PDF
# 	- The output file should be: LASTNAME_FIRSTNAME.pdf

from ast import In
import json
import os
from turtle import fillcolor
from fpdf import FPDF

#json loc
cdirectory = os.getcwd()
print(cdirectory)
jsonfile = "%s/%s" % (cdirectory, "rbfresume.json")
jsondata = {}

#store in json
with open(jsonfile) as data_file:
    jsondata = json.load(data_file)

#personal deets
fname = jsondata ["firstname"]
mname = jsondata ["middlename"]
lname = jsondata ["lastname"]
abt = jsondata ["about"]
bday = jsondata ["birthday"]
Age = jsondata ["age"]
Sex = jsondata ["sex"]

#contact deets
eemail = jsondata ["email"]
fb = jsondata ["facebook"]
ig = jsondata ["instagram"]
twt = jsondata ["twitter"]
pint = jsondata ["pinterest"]
pnumber = jsondata ["phone number"]

#skills
sskills = jsondata ["skills"]

#educational bg
ccollege = jsondata ["college"]
cprogram = jsondata ["college program"]
shs = jsondata ["senior high school"]
sstrand = jsondata ["strand"]
jhs = jsondata ["junior high school"]

#create pdf file

pdf = FPDF ("P", "cm", "A4")
pdf.add_page()

class PDF(pdf):
    #for header
    def header ():
        pdf.set_font('Helvetica', 24)
        pdf.set_fill_color(247, 229, 205)
        pdf.set_text_color(40, 36, 29)
        pdf.cell (0, 5, fname + mname + lname, In = 1, align='L', fill =1 )
        pdf.image('sqrpic.jpg',17, 1, 7 )
    #for body
    def body ():
        pdf.cell (0, 1, align= 'L', In = 1)
    #for footer


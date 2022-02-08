# PDF Resume Creator
# 	- Create a python program that will create your personal resume in PDF format
# 	- All personal details are stored in a JSON file
# 	- Your program should read the JSON file and write the details in the PDF
# 	- The output file should be: LASTNAME_FIRSTNAME.pdf

import email
import json
import os
from ast import In
from textwrap import fill
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
aage = jsondata ["age"]
ssex = jsondata ["sex"]

#contact deets
eemail = jsondata ["email"]
fb = jsondata ["facebook"]
ig = jsondata ["instagram"]
twt = jsondata ["twitter"]
pint = jsondata ["pinterest"]
pnumber = jsondata ["phone number"]

#skills
sskills = jsondata ["skills"]
sskills1 = jsondata ["skills1"]
sskills2 = jsondata ["skills2"]

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
    pdf.set_margins(2,2)
    #for header
    def header ():
        pdf.set_font('Helvetica', 24)
        pdf.set_fill_color(247, 229, 205)
        pdf.set_text_color(40, 36, 29)
        pdf.cell (0, 6, fname + mname + lname, In = 0, align='R', fill =1 )
        pdf.image('sqrpic.jpg',10, 10, 6 )
        pdf.ln(2)
    #for body
    def body ():
        pdf.set_draw_color (40, 36, 29)
        #about me part
        pdf.set_font('Helvetica', 20)
        pdf.set_fill_color(40, 36, 29)
        pdf.set_text_color(247, 229, 205)
        pdf.cell (0, 3, "ABOUT ME", align="C", In = 1, fill= 1 )
        pdf.ln(1)
        pdf.set_font('Helvetica', 16)
        pdf.set_text_color(40, 36, 29)
        pdf.set_fill_color(247, 229, 205)
        pdf.cell (0, 4, abt, In = 1, align= "C", fill = 1)
        pdf.ln(2)
        pdf.set_font('Helvetica', 20)
        pdf.set_fill_color(40, 36, 29)
        pdf.set_text_color(247, 229, 205)
        pdf.cell (0, 3, "SKILLS", align="C", In = 1, fill= 1 )
        pdf.ln(1)
        pdf.set_font('Helvetica', 16)
        pdf.set_text_color(40, 36, 29)
        pdf.set_fill_color(247, 229, 205)
        pdf.cell (0, 1, sskills, In = 1, align= "C", fill = 1)
        pdf.cell (0, 1, sskills1, In = 1, align= "C", fill = 1)
        pdf.cell (0, 1, sskills2, In = 1, align= "C", fill = 1)
        pdf.ln(2)
        #personal deets
        pdf.set_font('Helvetica', 20)
        pdf.set_fill_color(40, 36, 29)
        pdf.set_text_color(247, 229, 205)
        pdf.cell (0, 3, "PERSONAL INFORMATION", align="C", In = 1, fill = 1 )
        pdf.ln(1)
        pdf.set_font('Helvetica', 16)
        pdf.set_text_color(40, 36, 29)
        pdf.set_fill_color(247, 229, 205)
        pdf.cell (0, 1,'BIRTHDAY: '+ bday, fill = 1, In = 1, align= "C")
        pdf.cell (0, 1, 'AGE: ' + aage, fill = 1, In = 1, align= "C")
        pdf.cell (0, 1, 'SEX: '+ ssex, fill = 1, In = 1, align= "C")
        pdf.ln(2)
        #contact info
        pdf.set_font('Helvetica', 20)
        pdf.set_fill_color(40, 36, 29)
        pdf.set_text_color(247, 229, 205)
        pdf.cell (0, 3, "CONTACT INFORMATION", align="C", In = 1, fill = 1 )
        pdf.ln(1)
        pdf.set_font('Helvetica', 16)
        pdf.set_text_color(40, 36, 29)
        pdf.set_fill_color(247, 229, 205)
        pdf.cell (0, 1, 'EMAIL: '+ eemail, fill = 1, In = 1, align= "C")
        pdf.cell (0, 1, 'PHONE NUMBER: '+ pnumber, fill = 1, In = 1, align= "C")
        pdf.cell (0, 1, 'FACEBOOK: '+ fb, fill = 1, In = 1, align= "C")
        pdf.cell (0, 1, 'INSTAGRAM: '+ ig, fill = 1, In = 1, align= "C")
        pdf.cell (0, 1, 'TWITTER: '+ twt, fill = 1, In = 1, align= "C")
        pdf.cell (0, 1, 'PINTEREST: '+ pint, fill = 1, In = 1, align= "C")
        pdf.ln(2)
        #educational bg
        
    #for footer


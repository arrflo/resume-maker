# PDF Resume Creator
# 	- Create a python program that will create your personal resume in PDF format
# 	- All personal details are stored in a JSON file
# 	- Your program should read the JSON file and write the details in the PDF
# 	- The output file should be: LASTNAME_FIRSTNAME.pdf

from ast import In
import json
import os
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
nname = jsondata ["name"]
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
pdf = FPDF ("P","cm","A4")
pdf.add_page ()


#for header
pdf.set_font("helvetica", "B", 20)
pdf.set_text_color(40, 36, 29)
pdf.set_fill_color(247, 229, 205)
pdf.cell(0, 5, "            " + nname, ln=1, align="L", fill=1)
pdf.image('sqrpic.jpg', 15, 1, 5)
pdf.ln(0.55)

pdf.set_font("helvetica", "B", 15)
pdf.set_text_color(247, 229, 205)
pdf.set_fill_color(40, 36, 29)
pdf.cell(0,1, "ABOUT ME", align="C", ln=1, fill=1)
pdf.set_font("helvetica", "", 15)
pdf.set_text_color(40, 36, 29)
pdf.set_fill_color(247, 229, 205)
pdf.cell(0,0.75, "" + abt, align="C", ln=1, fill=1)
pdf.ln(0.55)

pdf.set_font("helvetica", "B", 15)
pdf.set_text_color(247, 229, 205)
pdf.set_fill_color(40, 36, 29)
pdf.cell(0,1, "SKILLS", align="C", ln=1, fill=1)
pdf.set_font("helvetica", "", 15)
pdf.set_text_color(40, 36, 29)
pdf.set_fill_color(247, 229, 205)
pdf.cell(0,0.75, "" + sskills, align="C", ln=1, fill=1)
pdf.cell(0,0.75, "" + sskills1, align="C", ln=1, fill=1)
pdf.cell(0,0.75, "" + sskills2, align="C", ln=1, fill=1)
pdf.ln(0.55)

pdf.set_font("helvetica", "B", 15)
pdf.set_text_color(247, 229, 205)
pdf.set_fill_color(40, 36, 29)
pdf.cell(0,1, "PERSONAL INFORMATION", align="C", ln=1, fill=1)
pdf.set_font("helvetica", "", 15)
pdf.set_text_color(40, 36, 29)
pdf.set_fill_color(247, 229, 205)
pdf.cell(0,0.75, "BIRTHDAY: " + bday, align="C", ln=1, fill=1)
pdf.cell(0,0.75, "AGE: " + aage, align="C", ln=1, fill=1)
pdf.cell(0,0.75, "SEX: " + ssex, align="C", ln=1, fill=1)
pdf.cell(0,0.75, "PHONE NUMBER: " + pnumber, align="C", ln=1, fill=1)
pdf.ln(0.55)

pdf.set_font("helvetica", "B", 15)
pdf.set_text_color(247, 229, 205)
pdf.set_fill_color(40, 36, 29)
pdf.cell(0,1, "SOCIALS", align="C", ln=1, fill=1)
pdf.set_font("helvetica", "", 15)
pdf.set_text_color(40, 36, 29)
pdf.set_fill_color(247, 229, 205)
pdf.cell(0,0.75, "EMAIL: " + eemail, align="C", ln=1, fill=1)
pdf.cell(0,0.75, "FACEBOOK: " + fb, align="C", ln=1, fill=1)
pdf.cell(0,0.75, "INSTAGRAM: " + ig, align="C", ln=1, fill=1)
pdf.cell(0,0.75, "TWITTER: " + twt, align="C", ln=1, fill=1)
pdf.cell(0,0.75, "PINTEREST: " + pint, align="C", ln=1, fill=1)
pdf.ln(0.55)

pdf.set_font("helvetica", "B", 15)
pdf.set_text_color(247, 229, 205)
pdf.set_fill_color(40, 36, 29)
pdf.cell(0,1, "EDUCATIONAL BACKGROUND", align="C", ln=1, fill=1)
pdf.set_font("helvetica", "", 15)
pdf.set_text_color(40, 36, 29)
pdf.set_fill_color(247, 229, 205)
pdf.cell(0,0.75, "COLLEGE: " + ccollege, align="C", ln=1, fill=1)
pdf.cell(0,0.75, "COLLEGE PROGRAM: " + cprogram, align="C", ln=1, fill=1)
pdf.cell(0,0.75, "SHS: " + shs, align="C", ln=1, fill=1)
pdf.cell(0,0.75, "SHS STRAND: " + sstrand, align="C", ln=1, fill=1)
pdf.cell(0,0.75, "JHS: " + jhs, align="C", ln=1, fill=1)


pdf.output ("FLORANDA_ROMALYN.pdf")





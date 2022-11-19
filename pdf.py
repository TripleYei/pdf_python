import PyPDF2
import sys
import pyfiglet

ascii_banner = pyfiglet.figlet_format("PDF READER")
print(ascii_banner)
# Creado por TripleYei

n = len(sys.argv)
print("Name", sys.argv[0])
print("Argumentos pasados", end = " ")
pdf = sys.argv[1]

pdfFileObj = open(pdf, 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
first_page = pdfReader.getPage(0)
print(first_page.extractText())

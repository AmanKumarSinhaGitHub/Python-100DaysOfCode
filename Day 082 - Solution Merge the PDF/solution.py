import os
os.chdir("Day 076 - Exercise Merge the PDF")

from PyPDF2 import PdfWriter

merger = PdfWriter()

for pdf in ["file1.pdf", "file2.pdf", "file3.pdf"]:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()

# Note : "pip3 install PyPDF2" run this command to install PyPDF2

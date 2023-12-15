import PyPDF2
import sys
import os

merger = PyPDF2.PdfMerger()
for file in os.listdir('Filepath of any directory'): # Enter the path of the directory where the pdf files are stored
    if file.endswith('.pdf'):
        merger.append(file)
merger.write('combined.pdf')

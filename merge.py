from PyPDF2 import PdfWriter
from pathlib import Path
import os

def get_pdf_files(directory):
    pdf_files = [os.path.join(directory, file) for file in os.listdir(directory) if file.lower().endswith('.pdf')]
    return pdf_files

# Replace 'your_directory_path' with the actual path of the directory you want to search
directory_path = 'src'

pdf_files = get_pdf_files(directory_path)

# Merge
merger = PdfWriter()

# Define the PDF files to merge
output = r'merged.pdf'
for file in pdf_files:
    fullpath = Path(file).resolve()
    merger.append(fullpath)

merger.write(output)
merger.close()

import PyPDF2
import textract

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

def pdf2txt(file_path: str) -> str:
    with open(file_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        texts = ''
        np = pdf_reader.getNumPages()
        for i in range(np):
            texts += pdf_reader.getPage(i).extractText()
    return texts
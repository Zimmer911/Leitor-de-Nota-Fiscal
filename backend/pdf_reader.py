import fitz  # PyMuPDF
from pdf2image import convert_from_path
import pytesseract
import os

# Define caminho do Tesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text_from_pdf(path):
    text = extract_direct_text(path)
    if not text.strip():
        print("📸 PDF escaneado. Aplicando OCR...")
        text = extract_text_with_ocr(path)
    else:
        print("📝 PDF com texto embutido. Extração direta.")
    return text

def extract_direct_text(path):
    text = ""
    doc = fitz.open(path)
    for page in doc:
        text += page.get_text()
    return text

def extract_text_with_ocr(path):
    images = convert_from_path(path)
    text = ""
    for image in images:
        text += pytesseract.image_to_string(image, lang="por")
    return text

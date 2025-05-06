import fitz
from pdf2image import convert_from_path
import easyocr
import os

# Inicializa o leitor OCR com português
reader = easyocr.Reader(['pt'])

def extract_text_from_pdf(path):
    """
    Extrai texto diretamente ou via OCR com EasyOCR.
    """
    text = extract_direct_text(path)
    
    if not text.strip():
        print("📸 PDF escaneado. Aplicando OCR (EasyOCR)...")
        text = extract_text_with_easyocr(path)
    else:
        print("📝 PDF com texto embutido. Extração direta.")
    
    return text

def extract_direct_text(path):
    """
    Usa PyMuPDF para tentar extrair texto embutido.
    """
    text = ""
    doc = fitz.open(path)
    for page in doc:
        text += page.get_text()
    return text

def extract_text_with_easyocr(path):
    """
    Extrai texto com EasyOCR a partir de imagens convertidas.
    """
    images = convert_from_path(path)
    full_text = ""

    for i, image in enumerate(images):
        image_path = f"temp_page_{i}.png"
        image.save(image_path)

        result = reader.readtext(image_path, detail=0)  # detail=0 → só texto
        page_text = "\n".join(result)
        full_text += page_text + "\n"

        os.remove(image_path)  # Limpa imagem temporária

    return full_text

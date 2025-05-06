from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import os
from datetime import datetime
import json
from typing import List

from pdf_reader import extract_text_from_pdf
from extract_fields import extract_fields
from database import SessionLocal, Documento
from sqlalchemy.orm import Session

app = FastAPI()

# Middleware de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pasta onde os arquivos serão salvos
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Rota principal para teste
@app.get("/")
def read_root():
    print("📡 Requisição GET à raiz recebida.")
    return {"message": "Hello World"}

# Rota para upload de PDF, extração e salvamento no banco
@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    print("📥 Recebendo upload...")

    try:
        file_location = os.path.join(UPLOAD_DIR, file.filename)
        print(f"📂 Salvando arquivo em: {file_location}")

        with open(file_location, "wb") as f:
            content = await file.read()
            f.write(content)

        print("✅ Upload concluído com sucesso!")

        # Etapa 1: Extrair texto do PDF
        texto_extraido = extract_text_from_pdf(file_location)

        # Etapa 2: Extrair campos com regex
        campos_extraidos = extract_fields(texto_extraido)

        # Etapa 3: Salvar no banco de dados
        db: Session = SessionLocal()
        novo_doc = Documento(
            cnpj=campos_extraidos["cnpjs"][0] if campos_extraidos["cnpjs"] else None,
            data=campos_extraidos["datas"][0] if campos_extraidos["datas"] else None,
            valor_total=campos_extraidos["valores"][0] if campos_extraidos["valores"] else None,
            json_extraido=json.dumps(campos_extraidos, ensure_ascii=False),
            caminho_pdf=file_location,
            data_upload=datetime.utcnow()
        )
        db.add(novo_doc)
        db.commit()
        db.refresh(novo_doc)

        # Retorno da resposta
        return JSONResponse(
            content={
                "filename": file.filename,
                "texto_extraido": texto_extraido,
                "campos_extraidos": campos_extraidos,
                "id_registro": novo_doc.id
            },
            status_code=200
        )

    except Exception as e:
        print(f"❌ Erro ao processar arquivo: {e}")
        return JSONResponse(content={"error": str(e)}, status_code=500)

# Rota para listar todos os documentos salvos
@app.get("/documentos/")
def listar_documentos():
    try:
        db: Session = SessionLocal()
        documentos = db.query(Documento).all()

        resultado = []
        for doc in documentos:
            resultado.append({
                "id": doc.id,
                "cnpj": doc.cnpj,
                "data": doc.data,
                "valor_total": doc.valor_total,
                "caminho_pdf": doc.caminho_pdf,
                "data_upload": doc.data_upload.strftime("%d/%m/%Y %H:%M:%S"),
                "json_extraido": json.loads(doc.json_extraido) if doc.json_extraido else {}
            })

        return JSONResponse(content=resultado)

    except Exception as e:
        print(f"❌ Erro ao listar documentos: {e}")
        return JSONResponse(content={"error": str(e)}, status_code=500)

# Importações principais do FastAPI e bibliotecas auxiliares
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

import os
from datetime import datetime
import json
from typing import List

# Importações de módulos internos do projeto
from pdf_reader import extract_text_from_pdf
from extract_fields import extract_fields
from database import SessionLocal, Documento
from sqlalchemy.orm import Session

# Criação da aplicação FastAPI
app = FastAPI()

# Configuração de CORS para permitir requisições do frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define a pasta onde os PDFs serão salvos
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Rota principal (teste rápido)
@app.get("/")
def read_root():
    print("📡 Requisição GET à raiz recebida.")
    return {"message": "Hello World"}

# Rota para upload de PDF, extração de texto e campos, e salvamento no banco
@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    print("📥 Recebendo upload...")

    try:
        # Salva o arquivo no disco
        file_location = os.path.join(UPLOAD_DIR, file.filename)
        print(f"📂 Salvando arquivo em: {file_location}")

        with open(file_location, "wb") as f:
            content = await file.read()
            f.write(content)

        print("✅ Upload concluído com sucesso!")

        # Etapa 1: Extrai texto (OCR se necessário)
        texto_extraido = extract_text_from_pdf(file_location)

        # Etapa 2: Extrai campos com regex
        campos_extraidos = extract_fields(texto_extraido)

        # Etapa 3: Salva no banco
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

# Rota para apagar todos os documentos e arquivos PDF
@app.delete("/documentos/limpar/")
def deletar_todos_documentos():
    """
    Deleta todos os registros do banco de dados e remove os PDFs da pasta uploads.
    """
    try:
        db: Session = SessionLocal()
        documentos = db.query(Documento).all()

        for doc in documentos:
            if doc.caminho_pdf and os.path.exists(doc.caminho_pdf):
                os.remove(doc.caminho_pdf)
            db.delete(doc)

        db.commit()
        return {"mensagem": f"{len(documentos)} documentos apagados com sucesso."}

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Erro ao apagar documentos: {str(e)}")

from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import os
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Adiciona o middleware de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todas as origens
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos
    allow_headers=["*"],  # Permite todos os cabeçalhos
)

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    print("📥 Recebendo upload...")

    try:
        file_location = os.path.join(UPLOAD_DIR, file.filename)
        print(f"📂 Salvando arquivo em: {file_location}")

        with open(file_location, "wb") as f:
            content = await file.read()
            f.write(content)

        print("✅ Upload concluído com sucesso! Arquivo salvo em:", file_location)

        return JSONResponse(content={"filename": file.filename}, status_code=200)
    except Exception as e:
        print(f"❌ Erro ao salvar arquivo: {e}")
        return JSONResponse(content={"error": str(e)}, status_code=500)

@app.get("/")
def read_root():
    print("📡 Requisição GET à raiz recebida.")
    return {"message": "Hello World"}

# Leitor Inteligente de Notas Fiscais

Este é um projeto de backend e frontend para leitura e extração de informações de Notas Fiscais em formato PDF. A aplicação permite o envio de arquivos PDF, realiza a leitura do conteúdo (texto ou imagem), extrai as informações relevantes (como CNPJ, Data, Valor Total) e armazena no banco de dados.

## 💪 Tecnologias Utilizadas

* **Backend**:

  * **FastAPI** - Framework rápido e moderno para a criação de APIs.
  * **PyMuPDF (fitz)** - Para extração de texto de PDFs com texto embutido.
  * **pdf2image** - Para converter PDFs com imagens em imagens.
  * **pytesseract** - OCR (Reconhecimento Óptico de Caracteres) para PDFs baseados em imagens.
  * **SQLite** - Banco de dados simples para armazenamento das notas extraídas.

* **Frontend**:

  * **React** - Biblioteca para a construção da interface do usuário.
  * **Vite** - Ferramenta de build para acelerar o desenvolvimento de projetos em React.
  * **Tailwind CSS** - Framework CSS para construção rápida e responsiva de interfaces.

## 🚀 Como Rodar o Projeto

### Passo 1: Clonar o Repositório

Clone o repositório para a sua máquina local:

```
git clone <URL_DO_REPOSITORIO>
cd leitor-inteligente-notas-fiscais
```

### Passo 2: Configuração do Backend (FastAPI)

Instalar as dependências do backend:

```bash
cd backend
pip install -r requirements.txt
```

#### Dependências utilizadas:

* fastapi
* pymupdf
* pdf2image
* pytesseract
* uvicorn
* sqlalchemy
* sqlite3 (já integrado ao Python)

### Instalar o Tesseract (necessário para OCR):

**Windows**:

* Baixe e instale o Tesseract OCR: [https://github.com/UB-Mannheim/tesseract/wiki](https://github.com/UB-Mannheim/tesseract/wiki)

**Linux**:

```bash
sudo apt-get install tesseract-ocr
```

### Rodar o servidor backend:

```bash
uvicorn main:app --reload
```

A API estará disponível em: [http://localhost:8000](http://localhost:8000)
Swagger: [http://localhost:8000/docs](http://localhost:8000/docs)

---

### Passo 3: Configuração do Frontend (React)

Instalar as dependências:

```bash
cd ../frontend
npm install
```

Rodar o servidor:

```bash
npm run dev
```

Frontend disponível em: [http://localhost:5173](http://localhost:5173)

---

## 🥮 Testar a Aplicação

### Backend:

* Acesse o endpoint [http://localhost:8000](http://localhost:8000) para verificar se o backend está funcionando.
* Utilize o Swagger em [http://localhost:8000/docs](http://localhost:8000/docs) para testar o upload.

### Frontend:

* Abra [http://localhost:5173](http://localhost:5173)
* Envie um arquivo PDF
* Veja os dados extraídos (CNPJ, data, valor) na interface
* Visualize a lista de documentos armazenados no banco

---

## 📄 Funcionalidades

* ✉️ **Envio de PDFs**
* 🔍 **Leitura e OCR** automática
* ♻️ **Extração de CNPJ, data, valor**
* 📂 **Armazenamento no banco SQLite**
* 📄 **Listagem dos documentos extraídos**
* 📆 **Data de upload registrada automaticamente**

---

## 🔧 Estrutura de Diretórios

```
leitor-inteligente-notas-fiscais/
├── backend/               # Código backend (FastAPI)
│   ├── main.py            # Arquivo principal do FastAPI
│   ├── pdf_reader.py      # Extração de texto/OCR
│   ├── extract_fields.py  # Regex para campos
│   ├── database.py        # Configuração do banco (SQLAlchemy)
│   ├── requirements.txt   # Dependências do backend
│   └── uploads/           # Pasta para armazenar PDFs enviados
├── frontend/              # Código frontend (React)
│   ├── src/
│   │   ├── App.jsx        # Componente principal com upload e listagem
│   │   └── App.css        # Estilo personalizado
│   ├── public/
│   └── package.json       # Dependências do frontend
└── README.md              # Este arquivo
```

---

## 🚫 Observação

* Certifique-se de manter o backend e frontend rodando simultaneamente.
* Verifique o CORS se for integrar com domínios diferentes (em produção).
* O banco de dados é local e simples (SQLite), mas pode ser substituído por PostgreSQL ou outro.

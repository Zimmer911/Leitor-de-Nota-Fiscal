# Leitor Inteligente de Notas Fiscais

Este é um projeto de backend e frontend para leitura e extração de informações de Notas Fiscais em formato PDF. A aplicação permite o envio de arquivos PDF, realiza a leitura do conteúdo (texto ou imagem), extrai as informações relevantes (como CNPJ, Data, Valor Total) e armazena no banco de dados.

## 🛠 Tecnologias Utilizadas

- **Backend**:  
  - **FastAPI** - Framework rápido e moderno para a criação de APIs.
  - **PyMuPDF (fitz)** - Para extração de texto de PDFs com texto embutido.
  - **pdf2image** - Para converter PDFs com imagens em imagens.
  - **pytesseract** - OCR (Reconhecimento Óptico de Caracteres) para PDFs baseados em imagens.
  - **SQLite** - Banco de dados simples para armazenamento das notas extraídas.

- **Frontend**:
  - **React** - Biblioteca para a construção da interface do usuário.
  - **Vite** - Ferramenta de build para acelerar o desenvolvimento de projetos em React.
  - **Tailwind CSS** - Framework CSS para construção rápida e responsiva de interfaces.


## 🚀 Como Rodar o Projeto

### Passo 1: Clonar o Repositório

Clone o repositório para a sua máquina local:

### Passo 2: Configuração do Backend (FastAPI)
Instalar as dependências do backend:
Navegue até a pasta do backend e instale as dependências:

cd backend

pip install -r requirements.txt


Dependências:


fastapi

pymupdf

pdf2image

pytesseract

uvicorn

sqlite3 (já integrado no Python)

### 2.Instalar o Tesseract (necessário para OCR):

Windows: Baixe e instale o Tesseract Installer.

Linux:
sudo apt-get install tesseract-ocr

### 3.Rodar o servidor backend:

Para rodar a aplicação backend, execute:

uvicorn main:app --reload

O servidor estará rodando em http://localhost:8000.


## Passo 3: Configuração do Frontend (React)


### 1.Instalar as dependências do frontend:

Navegue até a pasta do frontend e instale as dependências:

cd frontend
npm install

### 2.Rodar o servidor frontend:

Para rodar o frontend com o Vite, execute:

npm run dev

O servidor estará rodando em http://localhost:5173.

## 🧪 Passo 4: Testar a Aplicação

### Backend:
- Acesse o endpoint [http://localhost:8000](http://localhost:8000) para verificar se o backend está funcionando corretamente.
- Envie um arquivo PDF através do frontend e veja a extração de texto sendo realizada.

### Frontend:
- Abra o navegador em [http://localhost:5173](http://localhost:5173) e faça upload de um arquivo PDF.
- O arquivo será enviado para o backend, o texto será extraído, e os dados aparecerão na interface.

---

## 📝 Funcionalidades

- **Envio de PDFs**: Faça upload de arquivos PDF através da interface web.
- **Leitura de PDFs**: O sistema tenta ler PDFs com texto embutido. Se o arquivo for uma imagem (por exemplo, uma nota fiscal escaneada), o OCR (pytesseract) é aplicado para extração de texto.
- **Extração de Dados**: Dados como CNPJ, data e valor total são extraídos utilizando expressões regulares.
- **Armazenamento no Banco de Dados**: As informações extraídas são armazenadas no banco de dados SQLite.

---

## 🔧 Estrutura de Diretórios

leitor-inteligente-notas-fiscais/
├── backend/ # Código backend (FastAPI)
│ ├── main.py # Arquivo principal do FastAPI
│ ├── requirements.txt # Dependências do backend
│ └── uploads/ # Pasta para armazenar PDFs enviados
├── frontend/ # Código frontend (React)
│ ├── src/
│ ├── package.json # Dependências do frontend
│ └── public/
└── README.md # Este arquivo


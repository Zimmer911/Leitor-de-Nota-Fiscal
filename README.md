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

```bash
git clone https://github.com/Zimmer911/leitor-inteligente-notas-fiscais.git


### Passo 2: Configuração do Backend (FastAPI)


Instalar as dependências do backend:

Navegue até a pasta do backend e instale as dependências:


fastapi

pymupdf

pdf2image

pytesseract

uvicorn

sqlite3 (já integrado no Python)


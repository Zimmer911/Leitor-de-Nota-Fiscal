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



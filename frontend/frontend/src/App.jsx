import React, { useState } from 'react';
import './App.css';

function App() {
  const [file, setFile] = useState(null);
  const [uploadStatus, setUploadStatus] = useState("");
  const [loading, setLoading] = useState(false);

  const handleFileChange = (e) => {
    const selectedFile = e.target.files[0];
    if (selectedFile?.type === "application/pdf") {
      setFile(selectedFile);
      console.log("📂 Arquivo selecionado:", selectedFile);
    } else {
      setFile(null);
      console.log("❌ Tipo de arquivo inválido!");
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
  
    if (!file) {
      alert("Selecione um arquivo primeiro!");
      return;
    }
  
    setLoading(true);
    setUploadStatus("Enviando...");
  
    const formData = new FormData();
    formData.append("file", file);
    console.log("📤 Enviando arquivo para o servidor...");
  
    try {
      const response = await fetch("http://localhost:8000/upload/", {
        method: "POST",
        body: formData,
      });
  
      // Log da resposta completa (incluindo status e cabeçalhos)
      console.log("📡 Status da resposta:", response.status);
      console.log("📡 Cabeçalhos da resposta:", response.headers);
  
      // Verificar se a resposta é JSON
      const responseData = await response.json();
      console.log("📡 Resposta do backend:", responseData);
  
      if (response.ok) {
        if (responseData.filename) {
          setUploadStatus(`✅ Arquivo enviado com sucesso: ${responseData.filename}`);
        } else {
          setUploadStatus("✅ Arquivo enviado com sucesso.");
        }
      } else {
        console.log("❌ Erro no backend. Status não OK.");
        setUploadStatus("❌ Erro ao enviar o arquivo.");
      }
    } catch (error) {
      console.log("❌ Erro de conexão com o servidor:", error);
      setUploadStatus("❌ Erro de conexão com o servidor.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <h2>Enviar PDF</h2>
      <form onSubmit={handleSubmit}>
        <input type="file" accept=".pdf" onChange={handleFileChange} />
        <button type="submit" disabled={loading || !file}>
          {loading ? "Enviando..." : "Enviar"}
        </button>
      </form>
      {uploadStatus && <p>{uploadStatus}</p>}
    </div>
  );
}

export default App;

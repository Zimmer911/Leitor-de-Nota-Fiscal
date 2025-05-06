import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [file, setFile] = useState(null);
  const [uploadStatus, setUploadStatus] = useState("");
  const [uploadData, setUploadData] = useState(null);
  const [documentos, setDocumentos] = useState([]);
  const [loading, setLoading] = useState(false);

  // Seleciona arquivo PDF
  const handleFileChange = (e) => {
    const selectedFile = e.target.files[0];
    if (selectedFile?.type === "application/pdf") {
      setFile(selectedFile);
      setUploadStatus("");
    } else {
      setFile(null);
      alert("❌ Tipo de arquivo inválido! Envie um PDF.");
    }
  };

  // Envia PDF para o backend
  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!file) {
      alert("Selecione um arquivo primeiro!");
      return;
    }

    setLoading(true);
    setUploadStatus("📤 Enviando...");

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await fetch("http://localhost:8000/upload/", {
        method: "POST",
        body: formData,
      });

      const responseData = await response.json();
      setUploadData(responseData);

      if (response.ok) {
        setUploadStatus(`✅ Sucesso! Arquivo ${responseData.filename} enviado.`);
        fetchDocumentos();
      } else {
        setUploadStatus("❌ Erro ao enviar o arquivo.");
      }
    } catch (error) {
      console.error("Erro:", error);
      setUploadStatus("❌ Erro ao conectar com o servidor.");
    } finally {
      setLoading(false);
    }
  };

  // Busca todos os documentos do backend
  const fetchDocumentos = async () => {
    try {
      const response = await fetch("http://localhost:8000/documentos/");
      const data = await response.json();
      setDocumentos(data);
    } catch (error) {
      console.error("Erro ao buscar documentos:", error);
    }
  };

  // Apaga todos os documentos (rota DELETE)
  const handleApagarTudo = async () => {
    const confirmar = window.confirm("Tem certeza que deseja apagar TODOS os documentos?");
    if (!confirmar) return;

    try {
      const response = await fetch("http://localhost:8000/documentos/limpar/", {
        method: "DELETE",
      });

      const result = await response.json();
      alert(result.mensagem || "Documentos apagados com sucesso.");
      fetchDocumentos(); // Atualiza a lista
    } catch (error) {
      console.error("Erro ao apagar documentos:", error);
      alert("Erro ao tentar apagar os documentos.");
    }
  };

  // Carrega documentos ao abrir a página
  useEffect(() => {
    fetchDocumentos();
  }, []);

  return (
    <div className="App">
      <h2>📎 Enviar Nota Fiscal (PDF)</h2>

      <form onSubmit={handleSubmit}>
        <input type="file" accept=".pdf" onChange={handleFileChange} />
        <button type="submit" disabled={loading || !file}>
          {loading ? "Enviando..." : "Enviar"}
        </button>
      </form>

      {uploadStatus && <p>{uploadStatus}</p>}

      {uploadData && (
        <div className="resultado">
          <h3>📝 Resultado da Extração</h3>
          <p><strong>CNPJ:</strong> {uploadData.campos_extraidos.cnpjs?.[0] || "Não encontrado"}</p>
          <p><strong>Data:</strong> {uploadData.campos_extraidos.datas?.[0] || "Não encontrada"}</p>
          <p><strong>Valor:</strong> {uploadData.campos_extraidos.valores?.[0] || "Não encontrado"}</p>
        </div>
      )}

      <hr />

      <h3>📂 Documentos Salvos</h3>

      {/* Botão para apagar tudo */}
      <button
        style={{
          marginBottom: "20px",
          backgroundColor: "#dc3545",
          color: "#fff",
          padding: "8px 16px",
          border: "none",
          cursor: "pointer",
          borderRadius: "4px"
        }}
        onClick={handleApagarTudo}
      >
        🗑️ Apagar Todos os Documentos
      </button>

      {/* Tabela de documentos */}
      {documentos.length === 0 ? (
        <p>Nenhum documento cadastrado ainda.</p>
      ) : (
        <table border="1" cellPadding="8" style={{ margin: "auto" }}>
          <thead>
            <tr>
              <th>ID</th>
              <th>CNPJ</th>
              <th>Data</th>
              <th>Valor</th>
              <th>Upload</th>
            </tr>
          </thead>
          <tbody>
            {documentos.map((doc) => (
              <tr key={doc.id}>
                <td>{doc.id}</td>
                <td>{doc.cnpj || "-"}</td>
                <td>{doc.data || "-"}</td>
                <td>{doc.valor_total || "-"}</td>
                <td>{doc.data_upload}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
}

export default App;

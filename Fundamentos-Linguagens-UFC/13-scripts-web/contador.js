const fs = require("fs");

fs.readFile("texto.txt", "utf8", (err, data) => {
  if (err) {
    console.error("Erro ao ler o arquivo:", err);
    return;
  }

  const linhas = data.split("\n");
  const palavras = data.split(/\s+/).filter(Boolean);
  const caracteres = data.replace(/\s/g, "");

  console.log("📄 Estatísticas do Arquivo:");
  console.log(`- Linhas: ${linhas.length}`);
  console.log(`- Palavras: ${palavras.length}`);
  console.log(`- Caracteres (sem espaços): ${caracteres.length}`);
});
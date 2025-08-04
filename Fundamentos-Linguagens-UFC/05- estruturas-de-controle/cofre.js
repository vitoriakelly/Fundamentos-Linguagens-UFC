const senhaSecreta = 7;
let sucesso = false;

console.log("=== Cofre Seguro ===");
for (let tentativa = 1; tentativa <= 3; tentativa++) {
    let entrada = prompt(`Tentativa ${tentativa}/3 - Digite a senha:`);

    if (parseInt(entrada) === senhaSecreta) {
        console.log("✅ Cofre aberto com sucesso!");
        sucesso = true;
        break;
    } else {
        console.log("❌ Senha incorreta.");
    }
}

if (!sucesso) {
    console.log("🔒 Cofre bloqueado após 3 tentativas.");
}

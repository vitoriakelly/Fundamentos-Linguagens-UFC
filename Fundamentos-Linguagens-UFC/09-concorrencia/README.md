#  Desafio 09 – Concorrência

## 🎯 Objetivo

Explicar a diferença entre **threads** e **processos**, e implementar um **exemplo prático de concorrência** utilizando Python.

---

## 📚 Diferença entre Threads e Processos

### ✅ Processos:
- São **programas independentes** em execução.
- Possuem **memória separada**.
- Comunicação entre processos é mais **complexa** (ex: pipes, sockets).
- Criados com `multiprocessing` em Python.

### ✅ Threads:
- São **linhas de execução dentro do mesmo processo**.
- Compartilham a mesma **memória e recursos**.
- Comunicação entre threads é mais **simples**, mas exige controle de sincronização (locks, semáforos).
- Criadas com `threading` em Python.

---


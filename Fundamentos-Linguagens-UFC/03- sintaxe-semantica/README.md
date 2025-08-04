#  Terceiro Desafio — Descrições Sintáticas e Semânticas

## 📌 Linguagem Fictícia: **FlowLang**

**FlowLang** é uma linguagem inventada para simular pequenos fluxos lógicos de controle com variáveis e comandos de saída. Ela serve como base para ilustrar análise sintática e semântica.

---

## 🎯 Objetivo

Criar uma mini-gramática e demonstrar exemplos de análise léxica, sintática e semântica.

---

## 📚 1. Gramática Sintática (em pseudocódigo)

```pseudocodigo
Programa     → Instrução+

Instrução    → Atribuição | Impressão | Condicional

Atribuição   → "def" IDENT "=" Expressão ";"
Impressão    → "out" IDENT ";"
Condicional  → "if" Expressao "then" Instrução "end"

Expressão    → Número | IDENT | Expressão "+" Expressão | Expressão "-" Expressão

IDENT        → Letra (Letra | Dígito)*
Número       → Dígito+

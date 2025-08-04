#  Desafio 12 – Programação Lógica

## 🎯 Objetivo

Modelar e resolver um problema lógico simples usando **sintaxe inspirada em Prolog**, com simulação em **pseudocódigo**.

---

## 📌 Domínio Escolhido: Genealogia

O objetivo é representar **relações familiares** e permitir consultas como:
- Quem é pai/mãe de quem?
- Quem são os irmãos?
- Quem é avô de quem?

---

## 🔢 Fatos e Regras

### ✅ Fatos (conhecimentos declarativos):

```prolog
pai(joao, maria).
pai(joao, jose).
mae(ana, maria).
mae(ana, jose).
pai(jose, laura).
mae(maria, lucas).

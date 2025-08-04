# 🚗 Desafio 08 – Programação Orientada a Objetos

## 🎯 Objetivo

Modelar uma hierarquia simples de classes utilizando **Programação Orientada a Objetos (POO)** em **Java**, com uso de **herança**, **atributos**, **métodos comuns e específicos**.

---

##  Domínio Escolhido: Veículos de Transporte

A modelagem representa veículos genéricos e tipos específicos como **Carro** e **Bicicleta**.

---

## 🏗️ Hierarquia de Classes

         Veiculo
        /       \
    Carro     Bicicleta

---

## 📦 Descrição das Classes

### ✅ Classe `Veiculo` (superclasse)
- Atributos:
  - `marca`
  - `modelo`
  - `ano`
- Métodos:
  - `exibirInfo()`

### ✅ Classe `Carro` (subclasse de Veiculo)
- Atributos adicionais:
  - `numPortas`
- Método:
  - `ligarMotor()`

### ✅ Classe `Bicicleta` (subclasse de Veiculo)
- Atributos adicionais:
  - `tipo` (ex: "montanha", "urbana")
- Método:
  - `pedalar()`

---

## 🧪 Execução Esperada (Main.java)

```text
Marca: Toyota
Modelo: Corolla
Ano: 2020
Portas: 4
Motor ligado!

Marca: Caloi
Modelo: Elite
Ano: 2021
Tipo: montanha
Pedalando...


## Como executar
javac src/*.java


## Como rodar
java -cp src Main

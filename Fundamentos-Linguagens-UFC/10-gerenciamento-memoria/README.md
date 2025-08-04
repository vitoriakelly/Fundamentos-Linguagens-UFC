#  Desafio 10 – Gerenciamento de Memória

## 🎯 Objetivo

Comparar como o gerenciamento de memória é feito em duas linguagens de programação distintas: **Java**, que possui **coleta de lixo (GC)** automática, e **C**, onde a alocação e liberação de memória são manuais.

---

## 🧾 Quadro Comparativo: Java vs C

| Aspecto                         | Java                                      | C                                          |
|---------------------------------|-------------------------------------------|---------------------------------------------|
| **Tipo de gerenciamento**       | Automático (Garbage Collector)            | Manual (`malloc`, `calloc`, `free`)         |
| **Responsabilidade do programador** | Baixa: o GC gerencia                      | Alta: o programador deve alocar e liberar   |
| **Coleta de lixo**              | Sim, feita pela JVM em background         | Não há: sem liberação, ocorre vazamento     |
| **Alocação de memória**         | `new` (objetos em heap)                   | `malloc`, `calloc`, `realloc`               |
| **Liberação de memória**        | Automática pelo GC                        | Deve ser feita com `free`                   |
| **Controle fino**               | Baixo                                     | Alto (controla exatamente quanto e quando)  |
| **Segurança contra vazamentos**| Alta, desde que não haja ciclos fortes    | Baixa: vazamentos são comuns por erro humano|
| **Performance**                 | Mais lenta por causa do GC                | Pode ser mais rápida, mas arriscada         |
| **Ambiente típico**             | Aplicações web, mobile, sistemas robustos | Sistemas embarcados, drivers, sistemas OS   |

---

## 🧠 Conclusão

- A **gestão de memória automática em Java** facilita o desenvolvimento e evita muitos erros, mas custa desempenho em certos contextos.
- A **gestão manual em C** é poderosa e eficiente, mas exige cuidado extremo para evitar problemas como **vazamentos de memória** e **acessos inválidos**.

Cada abordagem tem seu espaço: Java é mais **seguro e moderno**, enquanto C oferece **controle total** e performance bruta para sistemas críticos.

---

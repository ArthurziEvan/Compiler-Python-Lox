# Projeto de Compilador Python - Lox

Este é um projeto de compilador educacional para a disciplina **Compiladores 1**, do professor Fabio Macedo Mendes, Universidade de Brasília (UnB); Faculdade de Ciências e Tencnologias em Engenharias (FCTE).

Utiliza a linguagem de programação Python, para interpretar LOX 
## 💡 Objetivo

Desenvolver um interpretador da linguagem Lox em Python, com foco educacional, demonstrando na prática os conceitos fundamentais de compiladores, como análise léxica e análise sintática 
---

## 💡 Descrição do Projeto

Este projeto consiste na implementação de um interpretador para a linguagem Lox, inspirado no livro *Crafting Interpreters*. A aplicação é responsável por ler código-fonte escrito em Lox, processá-lo por meio das etapas clássicas de um compilador e executar as instruções.

O sistema realiza:

* Análise léxica (tokenização do código)
* Análise sintática (geração de árvore de sintaxe abstrata - AST)
* Interpretação e execução do código
* Suporte inicial a expressões matemáticas e estruturas básicas da linguagem

---

## 🗂 Estrutura de Pastas

```bash
lox/
├── main.py            # Ponto de entrada do interpretador
├── scanner.py         # Análise léxica (gera tokens)
├── parser.py          # Análise sintática (gera AST)
├── interpreter.py     # Execução da AST
├── tokens.py          # Definição dos tipos de tokens
├── ast.py             # Estrutura da árvore sintática
└── README.md
```

---

## 📁 Descrição das Pastas

### `scanner.py`

Responsável por transformar o código-fonte em uma sequência de tokens.  Vai fazer a análise Léxica

### `tokens.py`

Define os tipos de tokens utilizados na linguagem, operadores, números, etc.. 

### `parser.py`

Responsável por analisar a sequência de tokens e construir a Árvore de Sintaxe Abstrata (AST)

### `ast.py`

Define as classes que representam os nós da árvore sintática, como expressões binárias e literais

### `interpreter.py`

Executa a AST gerada pelo parser e vê expressões, produzindo resultado

### `main.py`

Ponto de entrada do sistema, responsável por integrar todas as etapas leitura do código, geração de tokens, parsing e execução

---

### ▶️ 4. Executar o interpretador


## 💡 Tecnologias Utilizadas

* Python
* POO

---

## 📚 Referência

Projeto inspirado no livro *Crafting Interpreters*, utilizado como base conceitual para implementação do interpretador, com base nas intruções dadas em sala de aula.

---

## 🧠 Autor e Licença
Projeto desenvolvido como ensino didático para disciplina de Compiladores.
Você pode reutilizar, modificar e compartilhar livremente.

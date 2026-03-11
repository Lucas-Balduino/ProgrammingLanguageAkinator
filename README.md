# 🧞‍♂️ Akinator de Linguagens de Programação

Um jogo interativo de terminal construído em Python que adivinha a linguagem de programação ou tecnologia que você está pensando! Este projeto foi desenvolvido para aplicar os conceitos fundamentais de **Sistemas Especialistas** e manipulação de dados persistentes.

## 📌 Sobre o Projeto

Este script simula um Sistema Especialista clássico. Ele faz perguntas investigativas de "sim" ou "não" para afunilar as possibilidades até chegar a um palpite final. O grande diferencial é o seu **aprendizado dinâmico**: se o programa não souber a linguagem em que você pensou, ele pede que você o ensine, salvando esse novo conhecimento de forma permanente!

### O que é um Sistema Especialista?
É um programa de Inteligência Artificial projetado para simular a capacidade de tomada de decisão de um especialista humano. Ele é composto por:
1. **Base de Conhecimento:** Onde ficam os dados e regras (neste caso, a nossa árvore de decisão em formato JSON).
2. **Motor de Inferência:** A lógica que navega pelas regras com base nas respostas do usuário (o nosso laço `while`).

Sistemas assim são usados na vida real para diagnósticos médicos, aprovação de crédito bancário e suporte técnico automatizado.

---

## ⚙️ Funcionalidades

* **Adivinhação Inteligente:** Começa com uma base de dados robusta contendo 17 tecnologias (Python, Java, C++, SQL, Assembly, etc.).
* **Aprendizado de Máquina (Machine Learning básico):** Se o sistema errar, ele aprende a nova tecnologia e a pergunta diferencial para não errar na próxima vez.
* **Persistência de Dados:** Todo o conhecimento aprendido é salvo automaticamente em um arquivo `memoriaAkinator.json`. Ao fechar e abrir o jogo, ele continuará inteligente.
* **Sistema de Reset:** Um menu inicial que permite apagar a memória e voltar a árvore de conhecimento para o "estado de fábrica".
* **Tratamento de Erros:** O sistema lida graciosamente com entradas inválidas (textos com espaços, letras maiúsculas ou palavras não reconhecidas), evitando que o programa quebre.

---

## 🛠️ Como Executar

**Pré-requisitos:** Você só precisa ter o [Python](https://www.python.org/) instalado na sua máquina. Não é necessário instalar bibliotecas externas, pois o projeto usa apenas módulos nativos (`json` e `os`).

1. Clone este repositório:
   ```bash
   git clone https://github.com/Lucas-Balduino/ProgrammingLanguageAkinator.git

2. Navegue até a pasta do projeto:
    ```bash
    cd ProgrammingLanguageAkinator

3. Execute o script principal:
    ```bash
    python SistemaEspecialista.py

---

## 🧠 Arquitetura do Código

O projeto foi modularizado nas seguintes funções principais:

* **`carregarArvore()`:** Tenta ler o arquivo JSON. Se for a primeira execução e o arquivo não existir, ele carrega a árvore de decisão inicial mapeada no código.
* **`salvarArvore(arvore)`:** Recebe o dicionário atualizado com o novo aprendizado e o converte/salva em um arquivo `.json` estruturado.
* **`akinatorLinguagens()`:** É o coração do jogo. Contém o motor de inferência (navegação pela árvore) e a rotina de aprendizado que pede a nova linguagem e a nova pergunta ao usuário em caso de erro.
* **`resetarMemoria()`:** Utiliza a biblioteca `os` para deletar fisicamente o arquivo JSON, resetando o progresso do jogador.
* **`menu_principal()`:** Interface de terminal que mantém o jogo rodando em um laço infinito até o usuário decidir sair.

---

## 🧪 Testes Validados

Durante o desenvolvimento, garantimos a robustez do sistema com os seguintes cenários:

* **Entradas Inválidas:** Digitar `  SIM  `, `talvez` ou `Sim` são tratados com `.lower().strip()`. Respostas fora do padrão disparam um aviso amigável sem interromper o jogo.
* **Caminho Feliz:** Navegar pela árvore respondendo corretamente leva ao palpite exato da linguagem pré-cadastrada, sem alterações na memória.
* **Expansão Correta:** Ao ensinar uma nova linguagem (ex: Ruby), o sistema altera o galho correto da árvore na RAM e espelha essa mudança perfeitamente no JSON.

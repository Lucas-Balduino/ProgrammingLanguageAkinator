import json
import os

#Lucas Gonçalves Balduino - 22409139

arquivoMemoria = "memoriaAkinator.json"

# Tenta abrir o arquivo de memoria e usa um dicionario de houver erro
def carregarArvore():
    try:
        with open(arquivoMemoria, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        arvoreDecisao = {
            "pergunta": "A linguagem (ou tecnologia) foi criada ANTES do ano de 1990?",
            "sim": {
                "pergunta": "Ela é focada exclusivamente em consultar e manipular bancos de dados?",
                "sim": "SQL",
                "nao": {
                    "pergunta": "É considerada a linguagem de mais baixo nível, usando mnemônicos mapeados diretamente para instruções de processador?",
                    "sim": "Assembly",
                    "nao": {
                        "pergunta": "Foi criada principalmente para aplicações de negócios, finanças e sistemas bancários de grande porte?",
                        "sim": "Cobol",
                        "nao": {
                            "pergunta": "É uma linguagem baseada em lógica matemática, muito usada nos primórdios da Inteligência Artificial?",
                            "sim": "Prolog",
                            "nao": {
                                "pergunta": "Foi desenvolvida especificamente para computação científica e engenharia de alto desempenho?",
                                "sim": "Fortran",
                                "nao": {
                                    "pergunta": "Ela possui suporte nativo a Orientação a Objetos (classes)?",
                                    "sim": "C++",
                                    "nao": "C"
                                }
                            }
                        }
                    }
                }
            },
            "nao": {
                "pergunta": "Essa tecnologia é usada exclusivamente para estruturar ou estilizar páginas web (sem lógica tradicional de programação)?",
                "sim": {
                    "pergunta": "Ela é usada para dar estilo, cor e layout à página (ex: margens, fontes)?",
                    "sim": "CSS",
                    "nao": "HTML"
                },
                "nao": {
                    "pergunta": "Ela foi criada especificamente para rodar nativamente no navegador do usuário (Front-end)?",
                    "sim": "JavaScript",
                    "nao": {
                        "pergunta": "Ela é fortemente associada ao framework Flutter para criação de aplicativos móveis?",
                        "sim": "Dart",
                        "nao": {
                            "pergunta": "Ela é mundialmente famosa por ser a base do ecossistema de jogos Unity?",
                            "sim": "C#",
                            "nao": {
                                "pergunta": "Seu mascote é um gopher (esquilo) e foi criada pelo Google com foco em concorrência?",
                                "sim": "Go",
                                "nao": {
                                    "pergunta": "Ela é amplamente conhecida por focar em extrema segurança de memória sem usar 'garbage collector'?",
                                    "sim": "Rust",
                                    "nao": {
                                        "pergunta": "Sua principal fama inicial foi ser embutida no HTML para criar sites dinâmicos (é a base do WordPress)?",
                                        "sim": "PHP",
                                        "nao": {
                                            "pergunta": "Ela usa tipagem dinâmica e obriga o uso de indentação (espaços) para definir blocos de código?",
                                            "sim": "Python",
                                            "nao": "Java"
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
        return arvoreDecisao

# Atualiza o arquivo de memória
def salvarArvore(arvore):
    with open(arquivoMemoria, "w", encoding="utf-8") as arquivo:
        json.dump(arvore, arquivo, ensure_ascii=False, indent=4)

def resetarMemoria():
    if os.path.exists(arquivoMemoria):
        os.remove(arquivoMemoria)
        print("🧹 Memória apagada com sucesso! O Akinator voltou ao estado de fábrica.")
    else:
        print("✨ A memória já está limpa! Nenhum arquivo para apagar.")

def akinatorLinguagens():
    print("Bem-vindo ao Akinator de Tecnologias! Pense em uma destas opções:")

    arvoreDecisao = carregarArvore()

    nodoAtual = arvoreDecisao
    pai = None
    direcao = None

    # Motor de Inferência
    while type(nodoAtual) == dict:
        print(nodoAtual["pergunta"])
        resposta = input("> ").lower().strip()
        
        if resposta not in ["sim", "nao"]:
            print("⚠️ Input inválido. Por favor, responda apenas com 'sim' ou 'nao'.\n")
            continue
            
        pai = nodoAtual
        direcao = resposta
        nodoAtual = nodoAtual[resposta]

    # Palpite final
    print(f"\n🔮 O Akinator diz: A tecnologia que você pensou é... {nodoAtual}!")
    
    # Rotina de Aprendizado
    acertou = input("Eu acertei? (sim/nao) > ").lower().strip()
    
    if acertou == "sim":
        print("🎉 Oba! Mais uma vitória para o Akinator!")
    else:
        print("Poxa, eu errei!")
        novaLinguagem = input("Qual linguagem você estava pensando? > ").strip()
        novaPergunta = input(f"Digite uma pergunta onde a resposta seja 'SIM' para {novaLinguagem} e 'NAO' para {nodoAtual}:\n> ").strip()
        
        # Atualiza o dicionário na memória RAM
        pai[direcao] = {
            "pergunta": novaPergunta,
            "sim": novaLinguagem,
            "nao": nodoAtual
        }
        
        # 2. Salva o dicionário atualizado no disco rígido!
        salvarArvore(arvoreDecisao)
        print("🧠 Obrigado! Cérebro atualizado com sucesso. Eu não errarei na próxima vez!")

def menuPrincipal():
    while True:
        print("\n" + "="*30)
        print("🤖 AKINATOR DE LINGUAGENS")
        print("="*30)
        print("1. Jogar")
        print("2. Resetar Memória (Apagar dados salvos)")
        print("3. Sair")
        
        escolha = input("\nEscolha uma opção (1-3): ").strip()
        
        if escolha == "1":
            akinatorLinguagens()
        elif escolha == "2":
            resetarMemoria()
        elif escolha == "3":
            print("👋 Até logo! Encerrando o programa...")
            break
        else:
            print("⚠️ Opção inválida. Digite 1, 2 ou 3.")

# Executa o jogo
menuPrincipal()
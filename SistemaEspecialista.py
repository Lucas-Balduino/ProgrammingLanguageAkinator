
# Recomendador de Linguagens

def sistemaEspecialista():
    arvoreDecisao = {
        "pergunta": "Você prefere linguagens onde é obrigatório declarar o tipo da variável (tipagem estática)?",
        "nao": {
            "pergunta": "Tem interesse em desenvolvimento web?",
            "sim": "JavaScript",
            "nao": "Python"
        },
        "sim": {
            "pergunta": "Você prefere linguagens de baixo nivel?",
            "sim": "C++",
            "nao": {
                "pergunta": "Você tem interesse em desenvolvimento de Jogos (Unity)?",
                "sim": "C#",
                "nao": "Java"
            }   
        }
    }

    nodoAtual = arvoreDecisao

    while type(nodoAtual) == dict:
        print(nodoAtual["pergunta"])
       
        resposta = input().lower().strip()
    
        if resposta not in ["sim","nao"]: 
            print("Input inválido, responda com 'sim' ou 'nao'.")
            continue
            
        nodoAtual = nodoAtual[resposta]

    print("A sua linguagem é "+ nodoAtual)

# Recomendador de Linguagens

def sistemaEspecialista():
    arvore_decisao = {
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

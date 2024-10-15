from collections import defaultdict

dicionario_palavras = {
    "Jofre": ["Python", "Java", "C++"],
    "Adair": ["Python", "Ruby"],
    "Carla": ["JavaScript", "Python"],
    "Diego": ["Java", "Ruby"],
    "Gabriel": ["JavaScript"],
    "Helena": ["Python", "C#"],
    "Isabela": ["Java", "Ruby", "Swift"],
    "Luan": ["Java", "Python"],
    "Lucas": ["Ruby", "JavaScript"],
}

frequencia_palavras = defaultdict(int)


for palavras in dicionario_palavras.values():
    for palavra in palavras:
        frequencia_palavras[palavra] += 1


palavras_unicas = {}
for chave, palavras in dicionario_palavras.items():
    unicas = [palavra for palavra in palavras if frequencia_palavras[palavra] == 1]
    palavras_unicas[chave] = unicas


for chave, unicas in palavras_unicas.items():
    print(f"As palavras únicas para {chave} são: {unicas}")

def contar_frequencia_palavras(texto):
    texto = texto.lower()
    pontuacao = ",.!?:;\"'()[]{}"
    for p in pontuacao:
        texto = texto.replace(p, "")

    palavras = texto.split()

    frequencia = {}
    for palavra in palavras:
        if palavra in frequencia:
            frequencia[palavra] += 1
        else:
            frequencia[palavra] = 1

    return frequencia


texto = "Hoje vou jogar e Albion e Lol, mas tambem quero jogar xadrez. Porem hoje quero estudar tambem."

frequencia_palavras = contar_frequencia_palavras(texto)

print(frequencia_palavras)

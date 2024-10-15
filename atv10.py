def mapear_palavras(texto, dicionario_substituicao):
    palavras = texto.split()

    palavras_mapeadas = {palavra: dicionario_substituicao.get(
        palavra, palavra) for palavra in palavras}

    return palavras_mapeadas


texto = "O gato esta no telhado. O cachorro esta no quintal."


dicionario_substituicao = {
    "gato": "felino",
    "cachorro": "canino",
    "esta": "encontra-se",
    "telhado": "cobertura",
    "quintal": "jardim"
}


resultado = mapear_palavras(texto, dicionario_substituicao)


print("Dicionário de palavras mapeadas:")
print(resultado)

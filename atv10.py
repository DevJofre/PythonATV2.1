def mapear_palavras(texto, dicionario_substituicao):
    # Dividir o texto em palavras
    palavras = texto.split()

    # Criar o dicionário mapeado
    palavras_mapeadas = {palavra: dicionario_substituicao.get(
        palavra, palavra) for palavra in palavras}

    return palavras_mapeadas


# Texto original
texto = "O gato esta no telhado. O cachorro esta no quintal."

# Dicionário de substituição
dicionario_substituicao = {
    "gato": "felino",
    "cachorro": "canino",
    "esta": "encontra-se",
    "telhado": "cobertura",
    "quintal": "jardim"
}

# Mapeamento das palavras no texto
resultado = mapear_palavras(texto, dicionario_substituicao)

# Exibir o dicionário resultante
print("Dicionário de palavras mapeadas:")
print(resultado)

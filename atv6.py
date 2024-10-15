def comprimir_dicionario(dicionario, limite):
    return {chave: valor for chave, valor in dicionario.items() if valor >= limite}


# Exemplo de dicionário
dicionario = {
    "a": 105,
    "b": 55,
    "c": 37,
    "d": 84,
    "e": 189
}

limite = 55

dicionario_comprimido = comprimir_dicionario(dicionario, limite)

print(f"Dicionário comprimido: {dicionario_comprimido}")

def ordenar_por_valor(dicionario):
    dicionario_ordenado = dict(
        sorted(dicionario.items(), key=lambda item: item[1], reverse=True))
    return dicionario_ordenado


dicionario = {
    "a": 10,
    "b": 5,
    "c": 3,
    "d": 8,
    "e": 1
}

dicionario_ordenado = ordenar_por_valor(dicionario)

print(f"Dicionário ordenado: {dicionario_ordenado}")

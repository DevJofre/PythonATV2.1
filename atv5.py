dicionario_circular = {
    "Fogo": "1",
    "Ar": "2",
    "Agua": "3",
    "Terra": "4"
}

primeira_chave = next(iter(dicionario_circular))

dicionario_circular["ultimo"] = primeira_chave

print(dicionario_circular)

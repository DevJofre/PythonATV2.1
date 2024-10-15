def criar_dicionario_aninhado(chaves, valor_final):
    dicionario = valor_final  
    for chave in reversed(chaves):  
        dicionario = {chave: dicionario} 
    return dicionario


chaves = ['nivel1', 'nivel2', 'nivel3', 'nivel4']
valor_final = "valor"

dicionario_aninhado = criar_dicionario_aninhado(chaves, valor_final)
print(dicionario_aninhado)

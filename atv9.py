# Exemplo de matriz 3x3
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

dicionario_matriz = {}

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        dicionario_matriz[(i, j)] = matriz[i][j]

print("Dicionário de matrizes:")
print(dicionario_matriz)

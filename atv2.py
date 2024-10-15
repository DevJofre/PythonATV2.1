User_Python = {  
    "Jofre": 25, 
    "Adair": 26,
    "Carla": 22,
    "Diego": 28,               
    "Fernanda": 27,
}

User_Java = {
    "Gabriel": 35,
    "Helena": 24,
    "Isabela": 29,
    "Luan": 31,
    "Lucas": 26
}

print(f"Os usuarios de Python sao: {User_Python}")

print(f"Os usuarios de Java sao: {User_Java}")

Progamador_Total = {**User_Java, **User_Python}

print(f"Esse sao o nome de todos os progamadores da empresa: {Progamador_Total}")

def pessoa_mais_velha():
    if Progamador_Total:
        pessoa = max(Progamador_Total, key=Progamador_Total.get)
        return pessoa, Progamador_Total[pessoa]
    else:
        return "O dicionário está vazio."
    
nome, idade = pessoa_mais_velha()
print(f"A pessoa mais velha é {nome} com {idade} anos.")
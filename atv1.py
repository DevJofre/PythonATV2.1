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

Progamadore_Total = {**User_Java, **User_Python}

print(f"Esse sao o nome de todos os progamadores da empresa: {Progamadore_Total}")
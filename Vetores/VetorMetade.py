# Criando um vetor para armazenar os valores calculados
vetor = []

# Recebendo os dez números do usuário
for i in range(10):
    numero = float(input(f"Digite o número {i + 1}: "))
    metade = numero / 2  # Calculando a metade do número
    vetor.append(metade)  # Adicionando a metade no vetor 

# Imprimindo os valores armazenados no vetor
print("Valores armazenados no vetor (metade de cada número):")
for valor in vetor:
    print(valor)

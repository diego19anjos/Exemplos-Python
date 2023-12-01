# Solicitando ao usuário o número de elementos para o vetor
num_elementos = int(input("Digite o número de elementos para o vetor: "))

# Inicializando o vetor
vetor = []

# Armazenando os elementos no vetor
for i in range(num_elementos):
    elemento = int(input(f"Digite o elemento {i + 1}: "))
    vetor.append(elemento)

# Exibindo o vetor original
print("Vetor original:", vetor)

# Invertendo o vetor e exibindo
vetor_invertido = vetor[::-1] #fatiamento
print("Vetor invertido:", vetor_invertido)

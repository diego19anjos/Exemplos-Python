# Inicializando o vetor com doze elementos
vetor = []
for i in range(12):
    elemento = int(input(f"Digite o elemento {i + 1}: "))
    vetor.append(elemento)

# Inicializando contadores para pares e ímpares
quantidade_pares = 0
pares = []
quantidade_impares = 0
impares = []

# Verificando os números pares e ímpares no vetor
for num in vetor:
    if num % 2 == 0:  # Se o número for divisível por 2 (ou seja, é par)
        quantidade_pares += 1
        pares.append(num)  # Adicionando o número à lista de pares
    else:
        quantidade_impares += 1
        impares.append(num)  # Adicionando o número à lista de ímpares

# Exibindo os resultados
print(f"Quantidade de números pares: {quantidade_pares}")
print(f"Números pares: {pares}")
print(f"Quantidade de números ímpares: {quantidade_impares}")
print(f"Números ímpares: {impares}")

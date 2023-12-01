numeros = []

# Solicitando que o usuário insira 10 números
for i in range(10):
    numero = int(input(f"Digite o número {i + 1}: "))
    numeros.append(numero)

pares = []
impares = []

# Separando os números pares e ímpares
for num in numeros:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

# Exibindo os números pares seguidos dos ímpares
print("Números pares:")
for par in pares:
    print(par)

print("\nNúmeros ímpares:")
for impar in impares:
    print(impar)

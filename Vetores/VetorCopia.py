
vetor_original = []

    # Ler valores para o vetor original
print("Insira 5 valores para o vetor:")
for i in range(5):
        valor = int(input(f"Digite o {i + 1}º valor: "))
        vetor_original.append(valor)

    # Copiar os valores para outro vetor
vetor_copia = vetor_original[:]

    # Mostrar os valores do vetor de cópia na tela
print("Valores do vetor de cópia:")
for valor in vetor_copia:
        print(valor)


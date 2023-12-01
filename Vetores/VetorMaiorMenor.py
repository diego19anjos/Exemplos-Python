
vetor = []
for i in range(0,5):
    valor = int(input(f"Digite o valor da posição {i + 1}: "))
    vetor.append(valor)

menor = vetor[0]
maior = vetor[0]
pos_maior = pos_menor = 0

for i in range(1, len(vetor)):
        if vetor[i] > maior:
            maior = vetor[i]
            pos_maior = i
        elif vetor[i] < menor:
            menor = vetor[i]
            pos_menor = i


print(f"O maior elemento é: {maior} e está na posição {pos_maior + 1}")
print(f"O menor elemento é: {menor} e está na posição {pos_menor + 1}")

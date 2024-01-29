
vetor = []
for i in range(12):
    valor = int(input(f"Digite o valor para a posição {i}: "))
    vetor.append(valor)


x = int(input("Digite o valor de X (posição no vetor): "))
y = int(input("Digite o valor de Y (posição no vetor): "))


if x < 0 or x >= len(vetor) or y < 0 or y >= len(vetor):
    print("Valores de X ou Y estão fora do intervalo válido.")
else:
    
    soma = vetor[x] + vetor[y]
    print(f"A soma dos valores nas posições {x} e {y} é: {soma}")

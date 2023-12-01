# Solicitando que o usuário insira 5 números reais para o vetor
vetor = []
for i in range(5):
    numero = float(input(f"Digite o número {i + 1}: "))
    vetor.append(numero)

# Verificando se há números repetidos
repetidos = False

for i in range(len(vetor)):
    for j in range(i + 1, len(vetor)):
        if vetor[i] == vetor[j]:
            repetidos = True
            break

if repetidos:
    print("Há números repetidos no vetor.")
else:
    print("Não há números repetidos no vetor.")

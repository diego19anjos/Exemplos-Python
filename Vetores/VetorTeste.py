max = 10
N = int(input("Quantos números você quer inserir (máximo 10)? "))
vetor: [float] = [0 for x in range(N)]


    # Ler N números reais

if N > max:
        print("Você inseriu um valor maior que o máximo permitido")
        N = max

print("Insira os números:")
for i in range(N):
        num = float(input(f"Digite o {i + 1}º número: "))
        vetor.append(num)

    # Mostrar os elementos do vetor
print("Elementos do vetor:")
for elemento in vetor:
        print(elemento)



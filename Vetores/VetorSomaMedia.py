
vetor = []

# Ler N números reais
n = int(input("Quantos números reais você quer inserir? "))

print("Insira os números:")
for i in range(n):
        numero = float(input(f"Digite o {i + 1}º número: "))
        vetor.append(numero)


print("Elementos do vetor:")
for elemento in vetor:
        print(elemento)

soma = sum(vetor)
media = soma / len(vetor)

print(f"Soma dos elementos: {soma}")
print(f"Média dos elementos: {media}")

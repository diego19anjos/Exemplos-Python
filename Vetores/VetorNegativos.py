
maximo = 10
vetor = []

    # Ler N números inteiros
n = int(input("Quantos números inteiros você quer inserir (máximo 10)?"))
if n > maximo:
        print("Você inseriu um valor maior que o máximo permitido")
        n = maximo

print("Insira os números:")
for i in range(n):
        num = int(input(f"Digite o {i + 1}º número: "))
        vetor.append(num)

print("Numeros Negativos encontrados")
for num in vetor:
    if num < 0:
           print(num)
       


# negativos = [num for num in vetor if num < 0]

# if negativos:
#         print("Números negativos lidos:")
#         for elemento in negativos:
#             print(elemento)
# else:
#         print("Não foram inseridos números negativos.")



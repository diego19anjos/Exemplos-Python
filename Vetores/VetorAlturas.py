
pessoas = []

    # Ler informações de N pessoas
n = int(input("Quantas pessoas deseja inserir? "))

for i in range(n):
        nome = input(f"Digite o nome da {i + 1}ª pessoa: ")
        idade = int(input(f"Digite a idade de {nome}: "))
        altura = float(input(f"Digite a altura de {nome} (em metros): "))

        pessoa = {'nome': nome, 'idade': idade, 'altura': altura}
        pessoas.append(pessoa)

# Calcular altura média
altura_total = sum(pessoa['altura'] for pessoa in pessoas)
altura_media = altura_total / len(pessoas)

# Calcular porcentagem de pessoas com menos de 16 anos e listar seus nomes
menor_de_16 = [pessoa['nome'] for pessoa in pessoas if pessoa['idade'] < 16]
porcentagem_menor_de_16 = (len(menor_de_16) / len(pessoas)) * 100

# Mostrar resultados na tela
print(f"\nAltura média das pessoas: {altura_media:.2f} metros")

print(f"\nPorcentagem de pessoas com menos de 16 anos: {porcentagem_menor_de_16:.2f}%")
if len(menor_de_16) > 0:
    print("Nomes das pessoas com menos de 16 anos:")
    for nome in menor_de_16:
            print(nome)
else:
    print("Não há pessoas com menos de 16 anos na lista.")

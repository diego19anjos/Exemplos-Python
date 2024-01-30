#Faça um algoritmo que pergunte ao usuário quantos anos ele tem, depois disso, escreva true no console, 
#caso ele já tenha alcançado a maioridade (18 anos), caso contrário escreva False

# maioridade: bool
# idade = int( input("Quantos anos você tem? ") )
# maioridade = idade >= 18
# print(maioridade)

idade = int(input("Quantos anos você tem?"))

if idade >= 18:
    print("True")
else:
    print("False")
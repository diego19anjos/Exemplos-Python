#Leia a distancia em ˆ Km e a quantidade de litros de gasolina consumidos por um carro
#em um percurso, calcule o consumo em Km/l e escreva uma mensagem de acordo com
#a tabela abaixo:

# CONSUMO    |  (Km/l)   |      MENSAGEM
# menor que  |  8        |    Venda o carro!
# entre      |  8 e 14   |      Economico! ˆ
# maior que  |  12       |   Super economico!


km_percorridos = float(input("Digite a distância percorrida em km: "))
litros_consumidos = float(input("Digite a quantidade de litros de gasolina consumidos: "))

consumo = km_percorridos / litros_consumidos

if consumo < 8:
    print("Venda o carro!")
elif 8 <= consumo <= 14:
    print ("Econômico!")
else:
    print("Super econômico!")


print(f"Consumo: {consumo:.2f} Km/l")
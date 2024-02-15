# Função para ler um vetor de 5 números inteiros
def ler_lista():
    lista = []
    for i in range(5):
        numero = int(input(f"Digite o {i+1}º número inteiro: "))
        lista.append(numero)
    return lista

# Função para calcular a soma dos números no vetor
def calcular_soma(lista):
    soma = sum(lista)
    return soma

# Função para calcular a multiplicação dos números no vetor
def calcular_multiplicacao(lista):
    multiplicacao = 1
    for numero in lista:
        multiplicacao *= numero
    return multiplicacao

# Função principal
def main():
    lista = ler_lista()
    
    # Mostrar os números do vetor
    print("Números no vetor:")
    for numero in lista:
        print(numero)

    # Calcular e mostrar a soma
    soma = calcular_soma(lista)
    print("Soma dos números:", soma)

    # Calcular e mostrar a multiplicação
    multiplicacao = calcular_multiplicacao(lista)
    print("Multiplicação dos números:", multiplicacao)

if __name__ == "__main__":
    main()

# Função para ler uma lista de 10 números reais
def ler_lista():
    lista = []
    for i in range(10):
        numero = float(input(f"Digite o {i+1}º número real: "))
        lista.append(numero)
    return lista

# Função para mostrar os números na ordem inversa
def mostrar_ordem_inversa(vetor):
    print("Números na ordem inversa:")
    for numero in reversed(vetor):
        print(numero)

# Função principal
def main():
    vetor = ler_lista()
    mostrar_ordem_inversa(vetor)

if __name__ == "__main__":
    main()
#Crie uma lista com os itens que você precisa comprar no mercado.
#Utilize a função len() para verificar quantos itens você precisa comprar.
#Imprima a lista com os itens e suas quantidades (se houver).

lista_compras = ["maçãs", "leite", "pães", "ovos", "banana"]

# Verifica quantos itens há na lista
numero_itens = len(lista_compras)

# Imprime a lista com os itens e quantidades
for item in lista_compras:
    print(f"- {item}")

print(f"\nTotal de itens: {numero_itens}")

# Crie uma lista com os nomes dos seus clientes.
# Utilize a função sort() para ordenar a lista em ordem alfabética.
# Utilize a função in para verificar se um determinado cliente está na lista.

lista_clientes = ["Ana", "João", "Maria", "Pedro", "Carlos"]

# Ordena a lista em ordem alfabética
lista_clientes.sort()

# Verifica se um determinado cliente está na lista
cliente_existe = "Paulo" in lista_clientes

# Imprime os resultados
print(f"Lista de clientes ordenada: {lista_clientes}")

if cliente_existe == True:
   print(f"O cliente está na lista")
else:
   print(f"O cliente não está na lista")

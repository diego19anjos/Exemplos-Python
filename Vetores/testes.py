# lista1 = [10,4,1,9,12,7,22]

# print(lista1)

# #lista1.sort()

# #lista1.insert(3,45)

# #lista1.append(5)


# lista1.pop(5)
# print(lista1)
# # print(lista_1)


# # # Parte 1: Remoção de Elementos

# # # Passo 1: Criar uma lista inicial
# lista = [10, 20, 30, 40, 50]

# # # Passo 2: Pedir ao usuário para inserir o elemento a ser removido
# elemento_deletado = int(input("Insira um elemento para remover da lista: "))

# # # Passo 3: Remover o elemento inserido pelo usuário
# if elemento_deletado in lista:
#      lista.remove(elemento_deletado)
#      print(f"Elemento {elemento_deletado} removido com sucesso.")
# else:
#      print("Elemento não encontrado na lista.")


# # # Passo 4: Imprimir a lista atualizada
# print("Lista atualizada:", lista)



# # Parte 2: Adição de Elementos

# # Passo 1: Utilizar a lista obtida após a remoção ou criar uma nova lista
# # lista = ...  # Utilize a lista obtida após a remoção da Parte 1 ou crie uma nova lista
lista = [10, 20, 30, 40, 50]

# # Passo 2: Pedir ao usuário para inserir um elemento e sua posição na lista
elemento_adicionar = int(input("Insira um elemento para adicionar na lista: "))
posicao = int(input("Insira a posição desejada para adicionar o elemento na lista: "))

# # Passo 3: Adicionar o elemento na posição especificada
if posicao >= 0 and posicao <= len(lista):
  lista.insert(posicao, elemento_adicionar)
  print(f"Elemento {elemento_adicionar} adicionado na posição {posicao} com sucesso.")
else:
  print("Posição inválida para adicionar o elemento.")

# # Passo 4: Imprimir a lista atualizada
print("Lista atualizada:", lista)

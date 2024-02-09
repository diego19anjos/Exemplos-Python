# Criando um dicionário vazio para armazenar os produtos e preços
produtos = {}

# Pedindo ao usuário para inserir os produtos e preços
for i in range(3):
    produto = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: R$"))
    produtos[produto] = preco

# Mostrando os produtos e preços na tela
print("\nProdutos e seus respectivos preços:")
for produto, preco in produtos.items():
    print(f"{produto}: R${preco:.2f}")

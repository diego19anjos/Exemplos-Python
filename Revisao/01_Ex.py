# Somar os digítos de um número menor que 100
numero = int(input("Digite um número menor que 100: "))
if numero >= 100:
  print("O numero deve ser menor que 100")
else:
 dezena = numero // 10
 unidade = numero % 10
 soma = dezena + unidade
 print(f"A soma dos digitos de {numero} é igual a: {soma}")
# Calcular os divisores de um número
n = int(input("Digite um numero: "))
print(f"Os divisores de {n} são: ")
for i in range(1, n + 1):
 if n % i == 0:
    print(i,end=" ") 
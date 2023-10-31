x = int(input("Informe dois numeros: "))
y = int(input())

while x != y:
    if x < y:
        print("CRESCENTE")
    else:
        print("DECRESCENTE")
    
    x = int(input("Digite outros dois numeros: "))
    y = int(input())

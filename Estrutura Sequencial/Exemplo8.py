import math

base = float(input("Informe a base do retangulo: "))
altura = float(input("Informe a altura do retangulo: "))

area = base * altura

perimetro = 2 * (base + altura) 
diagonal = math.sqrt(math.pow(base,2)) + math.pow(altura,2)

print(f"Area: {area:.4f}")
print(f"Perimetro: {perimetro:.4f}")
print(f"Diagonal: {diagonal:.4f}")
import math  # Importe a biblioteca math para usar o valor de pi

# Ler o valor do raio do círculo
raio = float(input("Digite o valor do raio do círculo: "))

# Calcular a área do círculo usando a fórmula
area = math.pi * raio ** 2

# Exibir a área com duas casas decimais
print(f"A área do círculo é: {area:.2f}")
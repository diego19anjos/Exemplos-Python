x: int
y: float

x = 5
y = 2 * x

print(x)
print(y)

#***************************************************************

print("bom dia", end="")
print("boa noite", end="")


#***************************************************************

x: int; y: int
x = 10
y = 20
print(x)
print(y)


#****************************************************************

x: float
x = 2.3456
print("{:.2f}".format(x))
print(f"{x:.2f}")

#****************************************************************

idade: int
salario: float
nome: str
sexo: str

idade = 32
salario = 4560.9
nome = "Maria Silva"
sexo = "F"

print(f"A funcionaria {nome}, sexo {sexo}, salario R$ {salario:.2f} reais e tem {idade} anos")

cont = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez')

while True:
  x = int(input('Digite um valor entre 0 e 10: '))
  if x >= 0 and x <= 10:
    break

print(f'o número digitado foi {cont[x]}')

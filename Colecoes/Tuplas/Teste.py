times_rj = ('Botafogo', 'Flamengo', 'Fluminense', 'Vasco')

print(type(times_rj)) 
print(times_rj) 


print(times_rj[2]) 

times_sp = ('Sao Paulo')
print(type(times_sp))

objeto_string = ('tesoura')
objeto_tupla = ('tesoura',)

print(type(objeto_string)) 
print(type(objeto_tupla)) 

vogais = ('a', 'e', 'i', 'o', 'u')

vogais[1] = 'E'

meses_do_ano = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro")

#Selecionando apenas os meses de verão (dezembro a fevereiro)
meses_de_verao = meses_do_ano[11:] + meses_do_ano[:2]

#Exibindo os meses de verão
print("Meses de Verão:")
for mes in meses_de_verao:
    print(mes)



# Crie uma lista com as tarefas que você precisa realizar durante o dia.
# Utilize a função append() para adicionar "trabalhar" a sua lista.
# Utilize a função remove() para remover "tomar café".
# Imprima a lista com as tarefas pendentes.

# lista_tarefas = ["acordar", "tomar café", "estudar", "fazer exercícios", "almoçar"]


lista_tarefas = ["acordar", "tomar café", "estudar", "fazer exercícios", "almoçar"]

# Adiciona uma nova tarefa à lista
lista_tarefas.append("trabalhar")

# Remove uma tarefa concluída da lista
lista_tarefas.remove("tomar café")

print(lista_tarefas)

# Imprime a lista com as tarefas pendentes
for tarefa in lista_tarefas:
    print(f"- {tarefa}")

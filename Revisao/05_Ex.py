total_turmas = int(input("Digite a quantidade de turmas: "))
total_alunos = 0

for i in range(1, total_turmas + 1):
    while True:
        num_alunos = int(input(f"Digite a quantidade de alunos na turma {i}: "))
        if num_alunos <= 40:
            total_alunos += num_alunos
            break
        else:
            print("O número de alunos por turma não pode exceder 40.")

media_alunos_por_turma = total_alunos / total_turmas
print(f"O número médio de alunos por turma é: {media_alunos_por_turma:.2f}")

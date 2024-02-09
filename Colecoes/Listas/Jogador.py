# Crie uma lista com os nomes dos jogadores de um time de futebol.
# Crie uma lista com os gols marcados por cada jogador na temporada.
# Utilize a função max() para encontrar o jogador que mais marcou gols.
# Utilize a função min() para encontrar o jogador que menos marcou gols.
# Calcule a média de gols marcados por jogador.

jogadores = ["João", "Maria", "Pedro", "Ana", "Carlos"]
gols = [10, 5, 8, 2, 12]

# Encontra o jogador que mais marcou gols
maior_marcador = jogadores[gols.index(max(gols))]

# Encontra o jogador que menos marcou gols
menor_marcador = jogadores[gols.index(min(gols))]

# Calcula a média de gols marcados
media_gols = sum(gols) / len(gols)

# Imprime os resultados
print(f"Maior artilheiro: {maior_marcador}")
print(f"Menor artilheiro: {menor_marcador}")
print(f"Média de gols: {media_gols}")

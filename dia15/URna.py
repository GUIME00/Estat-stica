import numpy as np

bolas = ['R','R','R','B','B']

n_sim = 10000

resultados = []


for _ in range(n_sim):

    np.random.shuffle(bolas)

sorteio = bolas[0]

resultados.append(sorteio)


resultados = np.array(resultados)

A = resultados == 'R'

B = np.arange(n_sim) % 2 == 1


P_sim = np.mean(A | B)

print(f"Exercício - Probabilidade (bola vermelha ou índice ímpar) ~ {P_sim:.2f}")


bolas = np.array(['R', 'R', 'R', 'B', 'B'])

n_sim = 10000


# Sorteia diretamente n_sim bolas (com reposição)

sorteios = np.random.choice(bolas, size=n_sim, replace=True)


# Eventos

A = sorteios == 'R' # Evento A: bola vermelha

B = np.arange(n_sim) % 2 == 1 # Evento B: índice ímpar


# Probabilidade de A ou B

P_sim = np.mean(A | B)


print(f"Exercício - Probabilidade (bola vermelha ou índice ímpar) ~ {P_sim:.2f}")
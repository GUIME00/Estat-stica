import numpy as np
from scipy import stats

notas_alunos = [82, 76, 88, 91, 69, 73, 85, 79, 90, 77, 84, 80]

media_notas = np.mean(notas_alunos)
desvio_ = np.std(notas_alunos, ddof=1)
print(f"\nMédia de notas: {media_notas:.2f}")
print(f"Desvio padrão: {desvio_:.2f}")

# Teste t (H0: média = 75)
t_stat2, p_valor2 = stats.ttest_1samp(notas_alunos, popmean=75)
print("t =", t_stat2, "p =", p_valor2)
# Interprete os resultados
alpha = 0.05
if p_valor2 < alpha:
    print("Rejeitamos a hipótese nula.")
else:
    print("Não rejeitamos a hipótese nula.")
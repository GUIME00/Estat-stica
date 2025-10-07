# Quantidade inicial de bolas
vermelhas_inicial = 3
verdes_inicial = 2

# Após retirar uma bola vermelha sem reposição
vermelhas_restantes = vermelhas_inicial - 1
verdes_restantes = verdes_inicial
total_restantes = vermelhas_restantes + verdes_restantes

# Probabilidade da próxima bola ser verde
probabilidade_verde = verdes_restantes / total_restantes

print(f"A probabilidade da próxima bola ser verde, dado que a primeira foi vermelha, é {probabilidade_verde:.2f}")
# Quantidade total de bolas na urna
total_bolas = 5 + 7

# Fórmula
prob_verm = 5 / total_bolas
print("Exercício - 1")
print(f"A probabilidade de sair uma bola de cor vermelha é: {prob_verm:.2f}")

# Número total de lados do dado
total_lados = 6

# Números maiores que 3
favoraveis = [4, 5, 6]

# Calculando a probabilidade
probabilidade = len(favoraveis) / total_lados

print("Exercício - 2")
print(f"A probabilidade de sair um número maior que 3 é {probabilidade:.2f}")

# Total de resultados possíveis ao lançar duas moedas
total_resultados = 4

# Resultados favoráveis para exatamente uma cara
favoraveis = 2

# Calculando a probabilidade
probabilidade = favoraveis / total_resultados

print("Exercício - 3")
print(f"A probabilidade de sair exatamente uma cara é {probabilidade:.2f}")

# Quantidade inicial de bolas
vermelhas_inicial = 3
verdes_inicial = 2

# Após retirar uma bola vermelha sem reposição
vermelhas_restantes = vermelhas_inicial - 1
verdes_restantes = verdes_inicial
total_restantes = vermelhas_restantes + verdes_restantes

# Probabilidade da próxima bola ser verde
probabilidade_verde = verdes_restantes / total_restantes

print("Exercício - 4")
print(f"A probabilidade da próxima bola ser verde, dado que a primeira foi vermelha, é {probabilidade_verde:.2f}")
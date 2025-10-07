# Qual a probabilidade de sair exatamente uma cara ao lançar duas moedas?
def probabilidade_uma_cara():
    resultados_possiveis = ['CC', 'CK', 'KC', 'KK']  # C = Cara, K = Coroa
    casos_favoraveis = ['CK', 'KC']  # Resultados com exatamente uma cara
    probabilidade = len(casos_favoraveis) / len(resultados_possiveis)
    return probabilidade
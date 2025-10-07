# Uma urna tem 3 bolas vermelhas e 2 verdes. Se uma bola é retirada sem reposição e sai vermelha, qual a probabilidade da próxima ser verde?
def probabilidade_verde_apos_vermelha():
    bolas_vermelhas = 3
    bolas_verdes = 2
    total_bolas = bolas_vermelhas + bolas_verdes

    # Probabilidade de retirar uma bola vermelha na primeira retirada
    prob_vermelha_primeira = bolas_vermelhas / total_bolas

    # Após retirar uma bola vermelha, restam 2 vermelhas e 2 verdes
    bolas_vermelhas -= 1
    total_bolas -= 1

    # Probabilidade de retirar uma bola verde na segunda retirada
    prob_verde_segunda = bolas_verdes / total_bolas

    # Probabilidade condicional: P(Vermelha na 1ª e Verde na 2ª)
    probabilidade_condicional = prob_vermelha_primeira * prob_verde_segunda
    return probabilidade_condicional
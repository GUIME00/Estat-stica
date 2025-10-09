import pandas as pd

dados = [2, 4, 4, 4, 5, 5, 7, 9]

# Variância e desvio padrão
serie = pd.Series(dados)
variancia = serie.var()
desvio_padrao = serie.std()
print(f'Variância: {variancia}')
print(f'Desvio Padrão: {desvio_padrao}')
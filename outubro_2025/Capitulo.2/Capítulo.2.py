import pandas as pd

dados = [10, 15, 20, 20, 25, 30, 35]

# Média, mediana e moda
media = sum(dados) / len(dados)
mediana = sorted(dados)[len(dados) // 2] if len(dados) % 2 != 0 else \
    (sorted(dados)[len(dados) // 2 - 1] + sorted(dados)[len(dados) // 2]) / 2
moda = pd.Series(dados).mode()[0]
print("Exercício - 5")
print(f'Média: {media}, Mediana: {mediana}, Moda: {moda}')

dados = [2, 4, 4, 4, 5, 5, 7, 9]

# Variância e desvio padrão
serie = pd.Series(dados)
variancia = serie.var()
desvio_padrao = serie.std()
print("Exercício - 6")
print(f'Variância: {variancia}')
print(f'Desvio Padrão: {desvio_padrao}')

dados = [5, 7, 8, 5, 10, 12, 15]

# Calcule média, mediana, valor mínimo, valor máximo e amplitude
serie = pd.Series(dados)
media = serie.mean()
mediana = serie.median()
valor_minimo = serie.min()
valor_maximo = serie.max()
amplitude = valor_maximo - valor_minimo
print("Exercício - 7")
print(f"Média: {media}, Mediana: {mediana}, Mínimo: {valor_minimo}, Máximo: {valor_maximo}, Amplitude: {amplitude}")
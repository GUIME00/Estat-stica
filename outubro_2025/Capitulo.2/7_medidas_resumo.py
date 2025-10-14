import pandas as pd

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
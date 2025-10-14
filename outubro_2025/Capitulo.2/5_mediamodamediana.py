import pandas as pd

dados = [10, 15, 20, 20, 25, 30, 35]
media = sum(dados) / len(dados)
mediana = sorted(dados)[len(dados) // 2] if len(dados) % 2 != 0 else \
    (sorted(dados)[len(dados) // 2 - 1] + sorted(dados)[len(dados) // 2]) / 2
moda = pd.Series(dados).mode()[0]
print("Exercício - 5")
print(f'Média: {media}, Mediana: {mediana}, Moda: {moda}')
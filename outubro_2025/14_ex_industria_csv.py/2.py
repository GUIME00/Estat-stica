import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('industria.csv', parse_dates=['Data'])

print("Exercício 14 - 2")
# Calcule a Receita Média de cada Produto
df['Receita'] = df[['Receita']].mean(axis=1)
print(df[['Data', 'Produto', 'Receita']])

# Gere um gráfico de barras da Receita Média por Produto
mean_revenue = df.groupby('Produto')['Receita'].mean().reset_index()
plt.figure(figsize=(10, 6))
sns.barplot(data=mean_revenue, x='Produto', y='Receita')
plt.title('Receita Média por Produto')
plt.xlabel('Produto')
plt.ylabel('Receita Média')
plt.show()

# Qual Produto tem maior Receita Média?
mean_revenue = df.groupby('Produto')['Receita'].mean()
max_revenue_product = mean_revenue.idxmax()
print(f'O produto com maior receita média é: {max_revenue_product}')

# Algum produto apresenta Receita Média significativamente menor? Qual?
min_revenue_product = mean_revenue.idxmin()
print(f'O produto com menor receita média é: {min_revenue_product}')
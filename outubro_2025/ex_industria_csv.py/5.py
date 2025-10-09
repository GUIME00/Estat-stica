import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('industria.csv', parse_dates=['Data'])

# Use groupby ou pivot_table para calcular a receita total para cada combinação de 'Fabrica' e 'Produto'
pivot_df = df.pivot_table(index='Fabrica', columns='Produto', values='Receita', aggfunc='sum', fill_value=0)
print(pivot_df)

# Heatmap com seaborn mostrando a receita total por fábrica e produto
plt.figure(figsize=(10, 6))
sns.heatmap(pivot_df, annot=True, fmt=".2f", cmap='YlGnBu')
plt.title('Receita Total por Fábrica e Produto')
plt.xlabel('Produto')
plt.ylabel('Fábrica')
plt.show()

# Qual produto gerou a maior receita total em cada fábrica?
max_revenue_products = pivot_df.idxmax(axis=1)
print("Produto com maior receita total por fábrica:")
print(max_revenue_products)

# Existe algum produto que nâo foi produzido ou vendido em alguma fábrica?
missing_products = pivot_df[pivot_df == 0].stack().index.tolist()
print("Produtos não produzidos ou vendidos em alguma fábrica:")
print(missing_products)
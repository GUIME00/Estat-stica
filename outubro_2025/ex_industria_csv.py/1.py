import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('industria.csv', parse_dates=['Data'])

# Calcule a Receita Total de cada Fábrica
factory_revenue = df.groupby('Fabrica')['Receita'].sum().reset_index()
print(factory_revenue)

# Gráfico de barras
plt.figure(figsize=(10, 6))
sns.barplot(data=factory_revenue, hue='Fabrica', y='Receita', palette='viridis', legend=False, x='Fabrica')
plt.title('Receita Total por Fábrica')
plt.xlabel('Fábrica')
plt.ylabel('Receita Total')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()

# Qual fábrica teve maior receita?
max_revenue_factory = factory_revenue.loc[factory_revenue['Receita'].idxmax()]
print(f'A fábrica com maior receita é: {max_revenue_factory["Fabrica"]} com receita de {max_revenue_factory["Receita"]}')

# Qual é a diferença entre a fábrica com maior receita e a com menor receita?
min_revenue_factory = factory_revenue.loc[factory_revenue['Receita'].idxmin()]
revenue_difference = max_revenue_factory['Receita'] - min_revenue_factory['Receita']
print(f'A diferença entre a maior e a menor receita é: {revenue_difference}')
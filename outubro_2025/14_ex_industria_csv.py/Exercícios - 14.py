import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('industria.csv', parse_dates=['Data'])

print("Exercício 14 - 1")
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
plt.show(block=False)

# Qual fábrica teve maior receita?
max_revenue_factory = factory_revenue.loc[factory_revenue['Receita'].idxmax()]
print(f'A fábrica com maior receita é: {max_revenue_factory["Fabrica"]} com receita de {max_revenue_factory["Receita"]}')

# Qual é a diferença entre a fábrica com maior receita e a com menor receita?
min_revenue_factory = factory_revenue.loc[factory_revenue['Receita'].idxmin()]
revenue_difference = max_revenue_factory['Receita'] - min_revenue_factory['Receita']
print(f'A diferença entre a maior e a menor receita é: {revenue_difference}')

print("Exercício 14 - 2")
# Calcule a Receita Média de cada Produto
df['Receita'] = df[['Receita']].mean(axis=1)
print(df[['Data', 'Produto', 'Receita']])

# Gere um gráfico de barras da Receita Média por Produto
mean_revenue = df.groupby('Produto')['Receita'].mean().reset_index()
plt.figure(figsize=(10, 6))
sns.barplot(data=mean_revenue, x='Produto', y='Receita')
plt.grid(True)
plt.title('Receita Média por Produto')
plt.xlabel('Produto')
plt.ylabel('Receita Média')
plt.show(block=False)

# Qual Produto tem maior Receita Média?
mean_revenue = df.groupby('Produto')['Receita'].mean()
max_revenue_product = mean_revenue.idxmax()
print(f'O produto com maior receita média é: {max_revenue_product}')

# Algum produto apresenta Receita Média significativamente menor? Qual?
min_revenue_product = mean_revenue.idxmin()
print(f'O produto com menor receita média é: {min_revenue_product}')

print("Exercício 14 - 3")
# Criar um coluna 'Mes' a partir da data de cada registro
df['Mes'] = df['Data'].dt.to_period('M')

# Calcule a quantidade total vendida por mês
monthly_sales = df.groupby('Mes')['Quantidade_Vendida'].sum()
monthly_sales.index = monthly_sales.index.to_timestamp()
monthly_sales = monthly_sales.reset_index()
monthly_sales.columns = ['Mes', 'Total_Vendido']
monthly_sales = monthly_sales.sort_values('Mes')

# Gráfico de linha mostrando a evolução da quantidade de vendas ao longo dos meses
plt.figure(figsize=(12, 6))
sns.lineplot(data=monthly_sales, x='Mes', y='Total_Vendido', marker='o')
plt.title('Evolução da Quantidade de Vendas ao Longo dos Meses')
plt.xlabel('Mês')
plt.ylabel('Quantidade Total Vendida')
plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()
plt.show(block=False)

# Qual mês teve a maior quantidade de vendas?
max_sales_month = monthly_sales.loc[monthly_sales['Total_Vendido'].idxmax()]
print(f'Mês com maior quantidade de vendas: {max_sales_month["Mes"].strftime("%Y-%m")} com {max_sales_month["Total_Vendido"]} unidades vendidas.')

# Existe tendência de aumento ou diminuição nas vendas ao longo do período?
correlation = monthly_sales['Mes'].astype(int).corr(monthly_sales['Total_Vendido'])
if correlation > 0:
    trend = 'aumento'
elif correlation < 0:
    trend = 'diminuição'
else:
    trend = 'estável'
print(f'Tendência nas vendas ao longo do período: {trend} (correlação: {correlation:.2f})')

print("Exercício 14 - 4")
# Cria a coluna 'Lucro' = 'Receita' - 'Custo'
df['Lucro'] = df['Receita'] - df['Custo']

# Calcule o lucro médio por fábrica usando groupby
lucro_medio = df.groupby('Fabrica')['Lucro'].mean().reset_index()
lucro_medio = lucro_medio.sort_values(by='Lucro', ascending=False)

# Crie um gráfico de barras mostrando olucro médio por fábrica
plt.figure(figsize=(10, 6))
sns.barplot(data=lucro_medio, hue='Fabrica', y='Lucro', palette='viridis', x='Fabrica')
plt.title('Lucro Médio por Fábrica')
plt.xlabel('Fábrica')
plt.ylabel('Lucro Médio')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show(block=False)

# Qual fábrica teve o maior lucro médio?
fabrica_mais_lucro = lucro_medio.iloc[0]
print(f"A fábrica com maior lucro médio é {fabrica_mais_lucro['Fabrica']} com um lucro médio de {fabrica_mais_lucro['Lucro']:.2f}")

# Alguma fábrica apresenta lucro negativo em algum registro?
fabrica_lucro_negativo = df[df['Lucro'] < 0]['Fabrica'].unique()
if len(fabrica_lucro_negativo) > 0:
    print("Fábricas com lucro negativo em algum registro:", fabrica_lucro_negativo)
else:
    print("Nenhuma fábrica apresentou lucro negativo em algum registro.")

print("Exercício 14 - 5")
# Use groupby ou pivot_table para calcular a receita total para cada combinação de 'Fabrica' e 'Produto'
pivot_df = df.pivot_table(index='Fabrica', columns='Produto', values='Receita', aggfunc='sum', fill_value=0)
print(pivot_df)

# Heatmap com seaborn mostrando a receita total por fábrica e produto
plt.figure(figsize=(10, 6))
sns.heatmap(pivot_df, annot=True, fmt=".2f", cmap='YlGnBu')
plt.title('Receita Total por Fábrica e Produto')
plt.xlabel('Produto')
plt.ylabel('Fábrica')
plt.show(block=False)

# Qual produto gerou a maior receita total em cada fábrica?
max_revenue_products = pivot_df.idxmax(axis=1)
print("Produto com maior receita total por fábrica:")
print(max_revenue_products)

# Existe algum produto que nâo foi produzido ou vendido em alguma fábrica?
missing_products = pivot_df[pivot_df == 0].stack().index.tolist()
print("Produtos não produzidos ou vendidos em alguma fábrica:")
print(missing_products)

input("Clique Enter para fechar as janelas plotadas...")
plt.close('all')
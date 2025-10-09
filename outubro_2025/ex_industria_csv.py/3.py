import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('industria.csv', parse_dates=['Data'])

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
plt.show()

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
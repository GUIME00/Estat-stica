import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1.
# Arquivo CSV com dados de voos
df = pd.read_csv('dados1.csv')

# 2.
# A: Carregar e explorar os dados
print(df.head())
print(df.info())
# Verificar valores nulos
print(df.isnull().sum())

# B: Estatísticas Descritivas
# Média, mediana, desvio-padrão e variância de: 
# Passageiros 
# Distância (km) 
# Ocupação (%) 
# Receita (R$)
stats = df[['Passageiros', 'Distância (km)', 'Ocupação (%)', 'Receita (R$)']].describe()
print(stats)

# Calcular o percentil 25%, 50%, 75% da receita.
percentiles = np.percentile(df['Receita (R$)'], [25, 50, 75])
print(f'Percentis da Receita (R$): {percentiles}')

# Encontrar a companhia com maior receita total e com maior número de passageiros.
max_revenue_company = df.groupby('Companhia Aérea')['Receita (R$)'].sum().idxmax()
max_passengers_company = df.groupby('Companhia Aérea')['Passageiros'].sum().idxmax()
print(f'Companhia com maior receita total: {max_revenue_company}')

# Contagem de voos por companhia.
flight_counts = df['Companhia Aérea'].value_counts()
print(flight_counts)

# Receita média por companhia e por aeroporto de origem.
mean_revenue_by_company = df.groupby('Companhia Aérea')['Receita (R$)'].mean()
mean_revenue_by_origin = df.groupby('Aeroporto de Origem')['Receita (R$)'].mean()

# C. Visualizações com Seaborn 
# Histograma da distribuição de passageiros. 
plt.figure(figsize=(10, 6))
sns.histplot(df['Passageiros'], bins=30, kde=True)
plt.title('Distribuição de Passageiros')
plt.xlabel('Número de Passageiros')
plt.ylabel('Frequência')
plt.show(block=False)

# Boxplot da ocupação (%) separada por companhia aérea.
plt.figure(figsize=(12, 6))
sns.boxplot(x='Companhia Aérea', y='Ocupação (%)', data=df)
plt.title('Ocupação (%) por Companhia Aérea')
plt.xlabel('Companhia Aérea')
plt.ylabel('Ocupação (%)')
plt.xticks(rotation=45)
plt.show(block=False)

# Gráfico de barras da receita média por companhia.
plt.figure(figsize=(12, 6))
sns.barplot(x=mean_revenue_by_company.index, y=mean_revenue_by_company.values)
plt.title('Receita Média por Companhia Aérea')
plt.xlabel('Companhia Aérea')
plt.ylabel('Receita Média (R$)')
plt.xticks(rotation=45)
plt.show(block=False)

# Scatterplot de distância x receita para verificar relação.
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Distância (km)', y='Receita (R$)', data=df)
plt.title('Distância vs Receita')
plt.xlabel('Distância (km)')
plt.ylabel('Receita (R$)')
plt.show(block=False)

# (Desafio) Heatmap de correlação entre variáveis numéricas (Passageiros, Distância (km), Ocupação (%), Receita (R$)).
plt.figure(figsize=(8, 6))
correlation_matrix = df[['Passageiros', 'Distância (km)', 'Ocupação (%)', 'Receita (R$)']].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Matriz de Correlação')
plt.show(block=False)

# D. Perguntas Analíticas 
# Qual companhia tem maior participação em número de voos?
most_flights_company = flight_counts.idxmax()
print(f'Companhia com maior número de voos: {most_flights_company}')

# A distância influencia a receita?
correlation_distance_revenue = df['Distância (km)'].corr(df['Receita (R$)'])
print(f'Correlação entre Distância e Receita: {correlation_distance_revenue}')

# Os voos com maior ocupação são necessariamente os de maior receita?
correlation_occupancy_revenue = df['Ocupação (%)'].corr(df['Receita (R$)'])
print(f'Correlação entre Ocupação e Receita: {correlation_occupancy_revenue}')

# Quais aeroportos de origem concentram mais voos?
most_flights_origin = df['Aeroporto de Origem'].value_counts().idxmax()
print(f'Aeroporto de origem com mais voos: {most_flights_origin}')

# 5️.  
# Usar groupby para analisar: 
# Receita média por mês.
df['Data do Voo'] = pd.to_datetime(df['Data do Voo'])
df['Mês'] = df['Data do Voo'].dt.month
mean_revenue_by_month = df.groupby('Mês')['Receita (R$)'].mean()
print(mean_revenue_by_month)

# Ocupação média por companhia.
mean_occupancy_by_company = df.groupby('Companhia Aérea')['Ocupação (%)'].mean()
print(mean_occupancy_by_company)

input("Pressione Enter para fechar tudo...")
plt.close('all')
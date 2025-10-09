import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('industria.csv', parse_dates=['Data'])

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
plt.show()

# Qual fábrica teve o maior lucro médio?
fabrica_mais_lucro = lucro_medio.iloc[0]
print(f"A fábrica com maior lucro médio é {fabrica_mais_lucro['Fabrica']} com um lucro médio de {fabrica_mais_lucro['Lucro']:.2f}")

# Alguma fábrica apresenta lucro negativo em algum registro?
fabrica_lucro_negativo = df[df['Lucro'] < 0]['Fabrica'].unique()
if len(fabrica_lucro_negativo) > 0:
    print("Fábricas com lucro negativo em algum registro:", fabrica_lucro_negativo)
else:
    print("Nenhuma fábrica apresentou lucro negativo em algum registro.")
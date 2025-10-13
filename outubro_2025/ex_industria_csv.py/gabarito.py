import pandas as pd
import matplotlib.pyplot as plt

# Lendo o CSV
df = pd.read_csv("industria.csv")

# Somando a receita por fábrica
receita_por_fabrica = df.groupby('Fabrica')['Receita'].sum()

# Fábrica com maior receita
fabrica_maior = receita_por_fabrica.idxmax()
receita_maior = receita_por_fabrica.max()

# Fábrica com menor receita
receita_menor = receita_por_fabrica.min()

# Diferença entre maior e menor receita
diferenca = receita_maior - receita_menor

print("Receita por fábrica:\n", receita_por_fabrica)
print(f"\nFábrica com maior receita: {fabrica_maior} ({receita_maior})")
print(f"Diferença entre maior e menor receita: {diferenca}")

# Calculando receita média por produto
media_receita_produto = df.groupby('Produto')['Receita'].mean()

# Produto com maior receita média
produto_maior_media = media_receita_produto.idxmax()
maior_media = media_receita_produto.max()

# Produto com menor receita média
produto_menor_media = media_receita_produto.idxmin()
menor_media = media_receita_produto.min()

print("Receita média por produto:\n", media_receita_produto)
print(f"\nProduto com maior receita média: {produto_maior_media} ({maior_media})")
print(f"Produto com menor receita média: {produto_menor_media} ({menor_media})")

# Convertendo a coluna Data para datetime
df['Data'] = pd.to_datetime(df['Data'])

# Extraindo o mês (formato YYYY-MM) para agrupar
df['Mes'] = df['Data'].dt.to_period('M')


# Somando a quantidade vendida por mês
venda_por_mes = df.groupby('Mes')['Quantidade_Vendida'].sum()

# Identificando o mês com maior quantidade vendida
mes_maior_venda = venda_por_mes.idxmax()
quantidade_maior = venda_por_mes.max()

print("Quantidade vendida por mês:\n", venda_por_mes)
print(f"\nMês com maior quantidade vendida: {mes_maior_venda} ({quantidade_maior})")

# Plotando gráfico para observar tendência
venda_por_mes.plot(kind='line', marker='o', title='Quantidade Vendida por Mês')

plt.xlabel('Mês')
plt.ylabel('Quantidade Vendida')
plt.grid(True)
plt.show()

# Calculando o lucro
df['Lucro'] = df['Receita'] - df['Custo']

# Lucro médio por fábrica
lucro_medio_fabrica = df.groupby('Fabrica')['Lucro'].mean()

# Fábrica mais lucrativa em média
fabrica_mais_lucrativa = lucro_medio_fabrica.idxmax()
maior_lucro_medio = lucro_medio_fabrica.max()

# Verificando se alguma fábrica tem lucro negativo em algum registro
lucro_negativo = df[df['Lucro'] < 0]

print("Lucro médio por fábrica:\n", lucro_medio_fabrica)
print(f"\nFábrica mais lucrativa em média: {fabrica_mais_lucrativa} ({maior_lucro_medio})")

if lucro_negativo.empty:
    print("Nenhuma fábrica apresenta lucro negativo em algum registro.")
else:
    print("Registros com lucro negativo:\n", lucro_negativo)

    # Receita total por fábrica e produto

receita_fabrica_produto = df.groupby(['Fabrica', 'Produto'])['Receita'].sum()

# Produto que gera mais receita em cada fábrica
produto_mais_receita = receita_fabrica_produto.groupby(level=0).idxmax().apply(lambda x: x[1])

print("Produto que gera mais receita em cada fábrica:\n", produto_mais_receita)

# Verificando produtos não produzidos/vendidos em cada fábrica

produtos = df['Produto'].unique()
faltantes_por_fabrica = {}

for fabrica in df['Fabrica'].unique():
    produtos_fabrica = df[df['Fabrica'] == fabrica]['Produto'].unique()

faltantes = [p for p in produtos if p not in produtos_fabrica]
faltantes_por_fabrica[fabrica] = faltantes

print("\nProdutos que não foram produzidos/vendidos em cada fábrica:")
for fabrica, faltantes in faltantes_por_fabrica.items():
    print(f"{fabrica}: {faltantes}")
import pandas as pd

# Carregar os dados
df = pd.read_csv("dados1.csv")  # ou use df = pd.read_clipboard() se colou direto

# Criar coluna de Rota
df['Rota'] = df['Aeroporto Origem'] + ' - ' + df['Aeroporto Destino']

# Calcular Receita por passageiro
df['ReceitaPorPassageiro'] = df['Receita (R$)'] / df['Passageiros']

# Agrupar por Companhia e Rota e calcular a média de Receita por Passageiro
eficiencia = df.groupby(['Companhia', 'Rota'])['ReceitaPorPassageiro'].mean().reset_index()

# Obter top 5 rotas mais eficientes por companhia
top5_por_companhia = (
    eficiencia.sort_values('ReceitaPorPassageiro', ascending=False)
    .groupby('Companhia')
    .head(5)
)

# Exibir resultado final
print(top5_por_companhia.sort_values(['Companhia', 'ReceitaPorPassageiro'], ascending=[True, False]))

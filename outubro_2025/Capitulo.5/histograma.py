import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Gere 1000 números aleatórios de uma distribuição normal( média=60, desvio padrão=15)
data = np.random.normal(loc=60, scale=15, size=1000)

# histograma com matplotlib
plt.figure(figsize=(10, 5))
plt.hist(data, bins=30, edgecolor='black')
plt.title('Histograma com Matplotlib')
plt.xlabel('Valor')
plt.ylabel('Frequência')
plt.show(block=False)

# histograma com seaborn
plt.figure(figsize=(10, 5))
sns.histplot(data, bins=30, kde=True)
plt.title('Histograma com Seaborn')
plt.xlabel('Valor')
plt.ylabel('Frequência')
plt.show(block=False)

input("Pressione Enter para fechar os gráficos...")
plt.close('all')
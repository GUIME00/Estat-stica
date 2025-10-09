import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

X = [1, 2, 3, 4, 5]
Y = [2, 4, 5, 4, 6]

# Plote o gráfico de dispersão (scatter plot) com seaborn
plt.figure(figsize=(8, 5))
sns.scatterplot(x=X, y=Y, s=100)
plt.title('Gráfico de Dispersão com Seaborn')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.grid(True)
plt.show()
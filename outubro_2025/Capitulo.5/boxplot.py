import seaborn as sns
import matplotlib.pyplot as plt

dados = [7, 8, 5, 6, 12, 14, 15, 8, 9, 10]
# Crie um boxplot com seaborn
plt.figure(figsize=(8, 5))
sns.boxplot(x=dados)
plt.title('Boxplot com Seaborn')
plt.xlabel('Valores')
plt.grid(True)
plt.show()
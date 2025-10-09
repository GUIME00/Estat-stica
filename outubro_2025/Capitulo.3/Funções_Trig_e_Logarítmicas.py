import numpy as np
import matplotlib.pyplot as plt

# Usando numpy, gere uma série de valores x (100 nºs entre 0.1 e 10) e calcule y = sin(x) + log(x)

x = np.linspace(0.1, 10, 100)
y = np.sin(x) + np.log(x)

plt.plot(x, y)
plt.title('Função: y = sin(x) + log(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()
import numpy as np

# Função para calcular f(x) = x^2 + 3x + 5
def funcao_quadratica(x):
    return x ** 2 + 3 * x + 5

valores = np.array([0, 1, 2, 3, 4, 5])
resultados = funcao_quadratica(valores)

print("Valores de x:", valores)
print("Resultados f(x):", resultados)
import numpy as np
from sklearn.linear_model import LinearRegression

tamanho = [50, 60, 70, 80, 90]
preco = [ 150, 200, 210, 240, 280]

# Ajuste um modelo de regressão linear e estime o preço de um imóvel de 100 m²
X = np.array(tamanho).reshape(-1, 1)
y = np.array(preco)
modelo = LinearRegression().fit(X, y)
preco_estimado = modelo.predict(np.array([[100]]))
print("Exercício - 10")
print(f"Preço estimado para um imóvel de 100 m²: R$ {preco_estimado[0]:.2f}")
import numpy as np
from sklearn.linear_model import LinearRegression

hrs_estudo = [1, 2, 3, 4, 5]
notas = [55, 60, 65, 70, 75]

# Ajuste uma regressão linear simples e interprete os coeficientes angular
X = np.array(hrs_estudo).reshape(-1, 1)
y = np.array(notas)
model = LinearRegression().fit(X, y)
slope = model.coef_[0]
intercept = model.intercept_
print("Exercício - 9")
print(f"Coeficiente angular (slope): {slope}")
print(f"Intercepto: {intercept}")

tamanho = [50, 60, 70, 80, 90]
preco = [ 150, 200, 210, 240, 280]

# Ajuste um modelo de regressão linear e estime o preço de um imóvel de 100 m²
X = np.array(tamanho).reshape(-1, 1)
y = np.array(preco)
modelo = LinearRegression().fit(X, y)
preco_estimado = modelo.predict(np.array([[100]]))
print("Exercício - 10")
print(f"Preço estimado para um imóvel de 100 m²: R$ {preco_estimado[0]:.2f}")
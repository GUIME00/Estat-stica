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
print(f"Coeficiente angular (slope): {slope}")
print(f"Intercepto: {intercept}")

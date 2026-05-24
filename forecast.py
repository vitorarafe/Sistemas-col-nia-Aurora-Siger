###regressão linear (oq vc tinha falado dan)
from data import parametro_X , parametro_Y
import numpy as np
import pandas as pd  
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Dados simulados
dados = {
    "parametro_X": parametro_X,
    "parametro_Y": parametro_Y,
}
df = pd.DataFrame(dados)

# Variavel independente (X)
X = df[["parametro_X"]]

# Variavel dependente (Y)
y = df["parametro_Y"]

# Criando modelo
modelo = LinearRegression()

# Treinando modelo
modelo.fit(X, y)

# Parametros da reta
print("Intercepto (β₀):", modelo.intercept_)
print("Inclinação (β₁):", modelo.coef_[0])

# Previsoes
y_pred = modelo.predict(X)

print("R²:", r2_score(y, y_pred)) #(coeficiente de determinação) qunato mais proximo de 1 melhor, se for negativo o modelo é pior que a media

# Simulação de previsão futura
novo_x = np.array([[81]])  # 81 e um valor aleatorio para o parametro_X, substitua por um valor real que faça sentido para a previsão que vocês querem fazer... 81 pq e mengao!

previsao = modelo.predict(novo_x)

print("Previsão futura:", previsao[0])

#Grafico
plt.scatter(X, y, color="blue", label="Dados observados")
plt.plot(X, y_pred, color="red", label="Regressão Linear")

plt.xlabel("parametro_X (unidade)")  # Substitua "unidade" pela unidade real do parâmetro X
plt.ylabel("parametro_Y (unidade)")  # Substitua "unidade" pela unidade real do parâmetro Y 
plt.title("Regressão Linear entre parametro_X e parametro_Y")  # Substitua pelo título real do gráfico

plt.legend()
plt.show()
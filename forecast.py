###regressão linear (oq vc tinha falado dan)
from data import incidencia_solar , energia_solar
import numpy as np
import pandas as pd  
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score


def prever_energia_futura():
# Dados simulados
    dados = {
        "solar": incidencia_solar,
        "energia": energia_solar,
    }
    df = pd.DataFrame(dados)

    # Variavel independente (X)
    X = df[["solar"]]

    # Variavel dependente (Y)
    y = df["energia"]

    # Criando modelo
    modelo = LinearRegression()

    # Treinando modelo
    modelo.fit(X, y)

    # Parametros da reta
    print("Intercepto (β₀):", modelo.intercept_)
    print("Inclinação (β₁):", modelo.coef_[0])
    # Previsoes
    y_pred = modelo.predict(X)
    r2 = r2_score(y, y_pred)
    print("R²:", r2) #(coeficiente de determinação) qunato mais proximo de 1 melhor, se for negativo o modelo é pior que a media

    # Simulação de previsão futura
    solar_futuro = np.array([[12]])  # KKKKKKKKKKKKKKKKKKK VAI CORINTHIANS 

    previsao = modelo.predict(solar_futuro)

    print(f"Previsão futura: {previsao[0]}")

    #Grafico
    plt.scatter(X, y, color="blue", label="Dados observados")
    plt.plot(X, y_pred, color="red", label="Regressão Linear")

    plt.xlabel("Incidência Solar") 
    plt.ylabel("Energia Gerada") 
    plt.title("Regressão Linear entre Incidência Solar e Energia Solar") 

    plt.legend()
    plt.show()
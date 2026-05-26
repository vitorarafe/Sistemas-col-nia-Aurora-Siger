# SGEC - Sistema de Gerenciamento Energético da Colônia 

## o que o sistema faz
 
1° **tabela hash** = dados organizados em dicionários no `data.py`: sistemas da nave e fontes de energia (solar e bateria).
 
2° **if** = decisões no `decison.py` com base na energia e consumo calculados pelo `energy.py` (se consumo > energia, se consumo < energia, se consumo == energia).
 
3° **função** = funções no `energy.py` para calcular energia total e consumo total, e funções no `decison.py` para tomar decisão e desligar sistemas.
 
4° **regressão linear** = no `forecast.py`, usa os dados de `incidencia_solar` e `energia_solar` do `data.py` para prever energia gerada.
 
5° **análise do uso de energia** = no `energy.py`, compara energia disponível (solar + bateria) com consumo dos sistemas ativos e sugere armazenar excedente ou emite alerta.
 
## como os dados estão organizados
 
1 - **organizar os dados da colônia** = no `data.py`: fontes de energia (solar 80 + bateria 150 = 230 no total), consumo de cada sistema (oxigenio 40, habitacao 30, comunicacoes 15, laboratorio 25 = 110 no total).
 
2 - **organizar sistemas** = no `data.py`: lista com os sistemas separados por tipo (essencial e pesquisa) e prioridade (1 = mais urgente).
 

## como rodar
 
```python
pip install numpy pandas matplotlib scikit-learn
python main.py
```
 
## entrada e saída
 
```python
# data.py
fontes_energia = { "solar": 80, "bateria": 150 }  # total = 230
 
sistemas = [
    { "nome": "Geração de Oxigênio", "consumo": 40, "tipo": "essencial" },
    { "nome": "Habitação",           "consumo": 30, "tipo": "essencial" },
    { "nome": "Comunicações",        "consumo": 15, "tipo": "essencial" },
    { "nome": "Laboratório",         "consumo": 25, "tipo": "pesquisa"  },
]
# consumo total = 110
```
 
```python
# saída do energy.py + decison.py
Energia Total Disponível: 230
Consumo Total de Energia: 110
Sugestão: Armazenar energia excedente
energia suficiente
```
 
```python
# saída do forecast.py com incidencia_solar = 12
Previsão futura: 27.04
R²: 0.99
```

## integrantes

Ana Carolina Freire Mafra, Daniel Guimarães Barreto, Paulo Henrique da Silva Gola, Vinicius Daniel de Borba e Vitor de Araujo Ferreira.

link do repositorio: [https://github.com/vitorarafe/Sistemas-col-nia-Aurora-Siger.git]
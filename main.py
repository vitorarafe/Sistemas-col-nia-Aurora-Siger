###execução do projeto
"""
SGEC - Sistema de Gerenciamento Energético da Colônia
"""

from decison import tomar_decisoes
from energy import analisar_energia 
from structure import buscar_maior_consumo, ordem_prioridade
from forecast import prever_energia_futura




analisar_energia()


tomar_decisoes()


maior = buscar_maior_consumo()
print(f"\nSistema com maior consumo: {maior['nome']}")

ordenados = ordem_prioridade()

for sistema in ordenados:
    print(f"{sistema['nome']}, Prioridade: {sistema['prioridade']}")


prever_energia_futura()

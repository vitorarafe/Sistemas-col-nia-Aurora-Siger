###analisa a energia na nave 

from data import sistemas, fontes_energia       # vou explicar para vocês, mas é a mesma coisa que eu falei do export default do react 

#energia total disponível com base nas fontes de energia
def calcular_energia_total(): 
        total = 0
        for valor in fontes_energia.values():
            total += valor
        return total


#criar uma função para calcular o consumo total de energia dos sistemas ativos ]]
def calcular_consumo_total(): 
        total = 0
        for sistema in sistemas:
            if sistema["ativo"]:
                 total += sistema["consumo"]
        
        return total

def analisar_energia():
    energia = calcular_energia_total()
    consumo = calcular_consumo_total()
    print(f"Energia Total Disponível: {energia}")
    print(f"Consumo Total de Energia: {consumo}")
    
    if consumo > energia:
        print("Alerta: Consumo de energia maior que a geração de energia!")
    elif energia - consumo > 50:
        print("Sugestão: Armazenar energia excendente")

    else: 
         print("Sistema energético estável")
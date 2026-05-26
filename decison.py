###toma as decisões da nave
from energy import calcular_energia_total, calcular_consumo_total

#vamos pensar para desenvolver isso. 

def tomar_decisoes():
    energia = calcular_energia_total()
    consumo = calcular_consumo_total()
    

#regras 

    if energia < 50 and consumo > 70:
        print("ALERTA!: Ativar modo de economia.")
       
    elif consumo > energia:
        print("ATENÇÃO!: Reduza levemente o consumo de energia.")
 
    else:
        print("Sistema energético estável.")


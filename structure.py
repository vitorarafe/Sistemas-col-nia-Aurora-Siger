###filas, pilhas e ordenação  
from data import sistemas


#fila 

fila_sistemas = [] 

for sistema in sistemas:
    fila_sistemas.append(sistema)


#função de busca  
def buscar_maior_consumo():
     
     maior = fila_sistemas[0]
       
     for sistema in sistemas:
            
            if sistema["consumo"] > maior["consumo"]:
                maior = sistema
     return maior


#ordenação por prioridade dos sistemas

def ordem_prioridade():
     
     return sorted(sistemas, key=lambda x: x['prioridade'])
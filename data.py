# ---------------- SISTEMAS DA NAVE ----------------

sistemas = [
    {
        "nome": "Geração de Oxigênio",
          "prioridade": 1
             "consumo":40,  
                "ativo": True,
                    "tipo": "essencial
    },
    {
        "nome": "laoratório",
          "prioridade":3
            "consumo":25,  
              "ativo": True,
                 "tipo": "pesquisa
    }

    {
        "nome": "Habitação",
            "prioridade": 1
              "consumo"30,  
                "ativo": True,
                  "tipo": "essencial"
    }

    {
        "nome": "Comunicações",
            "prioridade": 2
              "consumo":15,  
                "ativo": True,
                  "tipo": "essencial"
    }
]

# ---------------- ENERGIA (placeholder) ----------------

fontes_energia = [
    "solar": 80,  
    "bateria": 150,
]

# ---------------- REGRESSÃO LINEAR (TESTE) ----------------

incidencia_solar = [5, 10, 15, 20, 25]   #mudei para ficar mais legível, depois me fala oq acha 
energia_solar  = [12, 20, 33, 42, 55]  #energia
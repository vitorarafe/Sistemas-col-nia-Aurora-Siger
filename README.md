# SGEC - Sistema de Gerenciamento Energético da Colônia

O SGEC é um sistema desenvolvido em Python para simular o gerenciamento de energia de uma colônia em Marte.

O sistema:
- monitora a energia disponível;
- calcula o consumo dos sistemas;
- toma decisões automáticas;
- prevê energia solar futura.

---

# Funcionalidades

## Organização dos dados
No arquivo `data.py`, os dados são organizados usando listas e dicionários.

Exemplos:
- sistemas da colônia;
- fontes de energia;
- dados de incidência solar.

---

## Decisões automáticas
No arquivo `decison.py`, o sistema verifica:
- se o consumo está maior que a energia;
- se há energia suficiente;
- se é necessário economizar energia.

---

## Cálculo de energia
No arquivo `energy.py`, o sistema:
- calcula a energia total;
- calcula o consumo total;
- analisa o uso de energia.

---

## Previsão de energia
No arquivo `forecast.py`, é utilizada regressão linear para prever a energia gerada com base na incidência solar.

Bibliotecas utilizadas:
- pandas
- matplotlib
- scikit-learn

---

# Estruturas de Controle

O arquivo `structure.py` utiliza estruturas de dados para organizar os sistemas.

## Fila
Os sistemas são inseridos em uma fila para serem processados em sequência.

## Pilha
Os alertas do sistema podem ser armazenados em uma pilha.

## Busca
A função `buscar_maior_consumo()` identifica o sistema com maior consumo de energia.

## Ordenação
A função `ordem_prioridade()` organiza os sistemas pela prioridade.

---

# Como rodar o projeto

## Instalar bibliotecas

```bash
pip install numpy pandas matplotlib scikit-learn
```

## Executar

```bash
python main.py
```

---

# Exemplo de saída

```bash
Energia Total Disponível: 230
Consumo Total de Energia: 110
Sugestão: Armazenar energia excedente
Energia suficiente
```

---

# Integrantes

- Ana Carolina Freire Mafra
- Daniel Guimarães Barreto
- Paulo Henrique da Silva Gola
- Vinicius Daniel de Borba
- Vitor de Araujo Ferreira

---

# Repositório

link do repositorio: [https://github.com/vitorarafe/Sistemas-col-nia-Aurora-Siger.git]
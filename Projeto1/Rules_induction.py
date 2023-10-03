'''
Universidade Estadual de Santa Cruz - UESC
Autores: Kauan Souza, Luíz Rosário e Vítor Coutinho
Disciplina: Inteligência Artificial

'''

def map_reader(file_name):
    '''
    Função responsável por ler os dados do arquivo csv e 
    armazená-los em um dicionário.

    Parâmetros: path do arquivo csv
    Retorno: dicionário com os dados do arquivo csv

    '''

    data = {} # Dicionário que armazena os dados do arquivo csv
    values = () # Tupla que armazena os valores de cada linha do arquivo csv

    with open(file_name, "r", encoding="utf-8") as archive:
        for line in archive:
            values = line.strip().split(",") # Separa os valores de cada linha do arquivo csv
            index = values[0] # Armazena o índice da linha

            # Armazena os valores da linha no dicionário
            data[index] = values[1:]
    return data

for key, value in map_reader("Projeto1/Teste.csv").items():
    print(f"{key}: {value}")
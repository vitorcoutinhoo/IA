"""
    Universidade Estadual de Santa Cruz - UESC
    Autores: Kauan Souza, Luíz Rosário e Vítor Coutinho
    Disciplina: Inteligência Artificial
"""

# OrderedDict --> dicionário ordenado para armazenar os possíveis valores de cada coluna
from collections import OrderedDict


def map_reader(file_name):
    """
    Função responsável por ler os dados do arquivo csv e
    armazená-los em uma lista com os nomes das colunas e
    uma matriz com os dados.

    Parâmetros: path do arquivo csv
    Retorno: Matriz com os dados do arquivo csv
    """

    header = []
    dados = []
    with open(file_name, "r", encoding="utf-8") as archive:
        header = archive.readline().strip().split(",")
        for line in archive:
            aux = line.strip().split(",")
            dados.append(aux)

    return header, dados


def get_values(header, data):
    """
    Função responsável por retornar os possíveis valores de
    cada coluna da matriz.

    Parâmetros: lista com os nomes das colunas e matriz com os dados
    Retorno: lista com os possíveis valores de cada coluna
    """

    num_colunas = len(data[0])
    possiveis_valores = []

    for col in range(num_colunas):
        valores_unicos = list(OrderedDict.fromkeys(row[col] for row in data))
        possiveis_valores.append(valores_unicos)

    aux = possiveis_valores[0]
    possiveis_valores.remove(aux)

    resultado = OrderedDict(zip(header, possiveis_valores))
    return resultado



    

# head --> lista com os nomes das colunas
# resp --> matriz com os dados
# values --> lista com os possíveis valores de cada coluna
head, resp = map_reader("Projeto1/dados.csv")
values = get_values(head, resp)

print(head)
print()

for i in resp:
    print(i)
print()

for i in values:
    print(i)

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
        Retorno: Lista com os dados do arquivo csv
    '''

    header = []
    dados = []
    with open(file_name, "r", encoding="utf-8") as archive:
        header = archive.readline().strip().split(",")
        for line in archive:
            line = line.strip().split(",")
            map_data = {}

            for i, header_value in enumerate(header):
                map_data[header_value] = line[i]

            dados.append(map_data)

    return dados, header

def get_values(dados, header):
    '''
        Função responsável por contar a quantidade de valores
        de cada atributo.

        Parâmetros: lista com os dados do arquivo csv e o cabeçalho
        Retorno: Dicionário com os possivéis valores de cada atributo
    '''

    values = {}
    for header_value in header:
        values[header_value] = []

    for dado in dados:
        for header_value in header:
            if dado[header_value] not in values[header_value]:
                values[header_value].append(dado[header_value])

    return values


data_list, headers = map_reader("Projeto1/Teste.csv")
possible_values = get_values(data_list, headers)

for value in data_list:
    print(value)

print()

for key, value in possible_values.items():
    print(key, value)

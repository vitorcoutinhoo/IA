"""
    Universidade Estadual de Santa Cruz - UESC
    Autores: Kauan Souza, Luíz Rosário e Vítor Coutinho
    Disciplina: Inteligência Artificial
"""

import pandas as pd

def get_data(path):
    '''
        Função que lê o arquivo csv e retorna os atributos e a classe
        do dataset.
    '''
    _data = pd.read_csv(path, sep=',')
        
    _attributes = _data.columns.values.tolist()
    _class = _attributes[-1]
    _attributes = _attributes[1:-1]

    return _data, _attributes, _class

def get_count(_data, _attributes, _class):
    '''
        Função que retorna a quantidade de cada atributo e classe.
    '''
    _count = {}
    for attr in _attributes:
        _count[attr] = {}
        for value in _data[attr].unique():
            _count[attr][value] = {}
            for _class_value in _data[_class].unique():
                _count[attr][value][_class_value] = 0

    for _, row in _data.iterrows():
        for attr in _attributes:
            _count[attr][row[attr]][row[_class]] += 1

    return _count

def get_proportions(count, data):
    '''
        Função que retorna a proporção de cada atributo e classe.
    '''
    total_count = data["Dia"].count()

    proportions = {}
    for attr, values in count.items():
        proportions[attr] = {}
        for value, class_counts in values.items():
            proportions[attr][value] = {c: round(count/total_count, 9) for c, count in class_counts.items()}
    return proportions


data, attributes, _class = get_data('Projeto1/dados.csv')
count = get_count(data, attributes, _class)

# arquivo csv
print(data)
print()

# Quantidades de sim e não para cada atributo
for key, values in count.items():
    print(key, values)
print()

# Proporções
prop = get_proportions(count, data)
for key, values in prop.items():
    print(key, values)

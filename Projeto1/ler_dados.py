"""
    Universidade Estadual de Santa Cruz - UESC
    Autores: Kauan Souza, Luíz Rosário e Vítor Coutinho
    Disciplina: Inteligência Artificial
"""

import pandas as pd

def obter_dados(caminho):
    '''Função para ler o arquivo CSV e retornar os atributos e a classe do conjunto de dados.'''
    dados = pd.read_csv(caminho, sep=",")

    atributos = dados.columns.values.tolist()
    classe = atributos[-1]
    atributos = atributos[1:-1]

    return dados, atributos, classe


def obter_contagem(dados, atributos, classe):
    '''Função para retornar a contagem de cada atributo e classe.'''
    contagem = {}
    for atributo in atributos:
        contagem[atributo] = {}
        for valor in dados[atributo].unique():
            contagem[atributo][valor] = {}
            for valor_classe in dados[classe].unique():
                contagem[atributo][valor][valor_classe] = 0

    for _, linha in dados.iterrows():
        for atributo in atributos:
            contagem[atributo][linha[atributo]][linha[classe]] += 1

    return contagem


def obter_proporcoes(contagem, dados):
    """
    Função que retorna a proporção de cada atributo e classe.
    """
    total_contagem = dados[dados.columns.values.tolist()[0]].count()

    proporcoes = {}
    for atributo, valores in contagem.items():
        proporcoes[atributo] = {}
        for valor, contagem_classes in valores.items():
            proporcoes[atributo][valor] = {
                c: round((contagem / total_contagem) * 100, 9)
                for c, contagem in contagem_classes.items()
            }
    return proporcoes


dados, atributos, classe = obter_dados(r"Projeto1\animais.csv")

# Imprimindo o arquivo CSV
print("Conjunto de dados do arquivo CSV:")
print(dados)
print()

# Quantidades de sim e não para cada atributo
contagem_dict = obter_contagem(dados, atributos, classe)
print("Quantidades de sim e não para cada atributo:")
for chave, valores in contagem_dict.items():
    df = pd.DataFrame.from_dict(valores)
    print(f"Atributo: {chave}")
    print(df)
    print()

# Proporções
prop = obter_proporcoes(contagem_dict, dados)
print("Proporções:")
for chave, valores in prop.items():
    df = pd.DataFrame.from_dict(valores)
    print(f"Atributo: {chave}")
    print(df)
    print()


# Função para calcular a confiabilidade positiva
def calcular_confianca_positiva(dados, antecedente, rotulo_classe):
    total_exemplos = len(dados)
    exemplos_positivos = dados[dados[rotulo_classe] == "positivo"]

    if len(exemplos_positivos) == 0:
        return 0.0

    classificados_corretamente = len(
        exemplos_positivos[exemplos_positivos[antecedente] == "positivo"]
    )

    return classificados_corretamente / len(exemplos_positivos)


# Carregar o conjunto de dados e fazer a preparação
dados, atributos, classe = obter_dados(r"Projeto1\animais.csv")

# Inicializar uma lista vazia para armazenar as regras
regras = []

# Definir um limiar de confiabilidade positiva
limiar_confianca = 0.07  # Ajustar conforme necessário

# Enquanto houver exemplos não cobertos
while len(dados) > 0:
    melhor_antecedente = None
    melhor_confianca = 0.0

    # Iterar sobre todas as combinações de atributos
    for atributo in atributos:
        confianca = calcular_confianca_positiva(dados, atributo, classe)

        if confianca > melhor_confianca and confianca >= limiar_confianca:
            melhor_antecedente = atributo
            melhor_confianca = confianca

    if melhor_antecedente is not None:
        # Adicionar a regra à lista de regras
        regras.append((melhor_antecedente, classe))

        # Remover exemplos cobertos pela regra
        dados = dados[dados[melhor_antecedente] != "positivo"]
    else:
        break  # Não foi possível encontrar uma regra com confiança positiva suficiente

# Imprimindo as regras descobertas
print("Regras Descobertas:")
for i, regra in enumerate(regras, 1):
    print(f"Regra {i}: Se {regra[0]} então {classe}")

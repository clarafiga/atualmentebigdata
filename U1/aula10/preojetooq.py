import random

def ordem_mesas():
    garcons = [
        "Garçom 1",
        "Garçom 2",
        "Garçom 3",
        "Garçom 4",
        "Garçom 5",
        "Garçom 6",
        "Garçom 7",
        "Garçom 8",
        "Garçom 9",
        "Garçom 10"
    ]

    mesas = list(range(1, 31))

    random.shuffle(mesas)

    distribuicao = {}

    for garcom in garcons:
        distribuicao[garcom] = []

    for i in range(30):
        garcom = garcons[i % 10]
        distribuicao[garcom].append(mesas[i])

    return distribuicao

resultado = ordem_mesas()

print(resultado)import random

def ordem_mesas():
    garcons = [
        "Garçom 1",
        "Garçom 2",
        "Garçom 3",
        "Garçom 4",
        "Garçom 5",
        "Garçom 6",
        "Garçom 7",
        "Garçom 8",
        "Garçom 9",
        "Garçom 10"
    ]

    mesas = list(range(1, 31))

    random.shuffle(mesas)

    distribuicao = {}

    for garcom in garcons:
        distribuicao[garcom] = []

    for i in range(30):
        garcom = garcons[i % 10]
        distribuicao[garcom].append(mesas[i])

    return distribuicao

resultado = ordem_mesas()

print(resultado)
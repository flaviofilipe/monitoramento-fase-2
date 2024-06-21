from client.src.sensores.temperatura import SensorTemperatura
from client.src.models import Temperatura


"""
    Gera leituras de temperatura
    :param quant: quantidade de leituras a serem geradas
    :return: lista de leituras de temperatura

    A complexidade do código é O(n), onde n é o total de leituras
    Portanto, sua complexidade é linear, cresce a medida que o
    total de leituras aumenta, pois há apenas um loop.
"""


def gerar(quant: int) -> list[Temperatura]:
    leituras = []

    for _ in range(quant):
        temperatura = Temperatura(SensorTemperatura().get_temperatura())
        leituras.append(temperatura)
    return leituras

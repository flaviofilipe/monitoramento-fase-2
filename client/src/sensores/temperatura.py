from client.src.domain.sensores import ISensorTemperatura
from random import uniform


def get_mock_temperatura() -> float:
    return round(uniform(0, 50), 2)


"""
    Sensor de Temperatura
    Retorna uma temperatura aleatória
    :return: float

    Complexidade: O(1)
"""


class SensorTemperatura(ISensorTemperatura):
    def get_temperatura(self) -> float:
        return get_mock_temperatura()

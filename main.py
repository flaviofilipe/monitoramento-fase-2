from src.models import Plantacao
from src.sensores.sensoriamento import gerar
from src.operacoes import (
    imprimir_plantacao,
    imprimir_temperatura,
    imprimir_status,
)

TOTAL_PLANTACAO = 10
TOTAL_LEITURA = 10


"""
    Gerando a leitura de N plantações
    contendo X leituras de temperatura

    Complexidade: O(N²)

    Esta função tem uma complexidade quadrática O(N²)
    Pois tem 2 loops aninhados:
    1º loop para criar as plantações
    2º loop para criar as leituras de temperatura
    E retorna uma lista de tuplas contendo plantação e temperaturas
"""


def leitura_das_plantacoes():
    plantacoes = []
    for i in range(TOTAL_PLANTACAO):
        plantacao = Plantacao(
            nome=f"Plantacao_{i+1}",
        )

        temperatura = gerar(TOTAL_LEITURA)

        plantacoes.append((plantacao, temperatura))

    return plantacoes


def main():
    plantacoes = leitura_das_plantacoes()

    imprimir_plantacao(plantacoes)

    print("\n", "-" * 50, "\n")

    imprimir_temperatura(plantacoes)

    print("\n", "-" * 50, "\n")

    imprimir_status(plantacoes)


if __name__ == "__main__":
    main()

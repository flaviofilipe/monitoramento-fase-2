import time
import requests
from client.src.sensores.sensoriamento import gerar_paralelo
from client.src.operacoes import (
    imprimir_plantacao,
    imprimir_temperatura,
    sort_temperaturas,
    PlantacaoTemperatura,
)

TOTAL_PLANTACAO = 10
TOTAL_LEITURA = 10
SERVER_URL = "http://127.0.0.1:8080/sensores/"

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


def leitura_das_plantacoes(
    quant_pantacoes=TOTAL_PLANTACAO, quant_leituras=TOTAL_LEITURA
) -> list[PlantacaoTemperatura]:
    plantacoes = []
    for i in range(quant_pantacoes):
        plantacao = f"Plantacao_{i+1}"

        temperatura = gerar_paralelo(quant_leituras, 10)

        plantacoes.append(PlantacaoTemperatura(plantacao, temperatura))

    return plantacoes


def fase_1_plantacoes(plantacoes: list[PlantacaoTemperatura]):
    print("\n", "-" * 50, "\n")
    imprimir_plantacao(plantacoes)


"""
    Usa a função imprimir_temperatura com a complexidade O(N²)
"""


def fase_2_temperaturas_desordenadas(plantacoes: list[PlantacaoTemperatura]):
    imprimir_temperatura(plantacoes)


"""
    Usa a função sort_temperaturas com a complexidade O(N²)
"""


def fase_2_1_temperaturas_ordenadas(plantacoes: list[PlantacaoTemperatura]):
    print("\n", "-" * 50, "\n")
    plantacoes_ordenadas = sort_temperaturas(plantacoes)
    imprimir_temperatura(plantacoes_ordenadas)


"""
    Faz o envio da lista para usar a função imprimir_status com a complexidade O(N³), no Servidor
"""


def fase_3_status(plantacoes: list[PlantacaoTemperatura]):
    print("\n", "-" * 50, "\n")
    plantacoes_dict = [
        {
            "plantacao": p.plantacao,
            "temperaturas": [{"value": t.get_value()} for t in p.temperaturas],
        }
        for p in plantacoes
    ]
    response = requests.post(SERVER_URL, json=plantacoes_dict)
    print(response.json())


def main():
    start_time = time.time()
    plantacoes = leitura_das_plantacoes()

    fase_1_plantacoes(plantacoes)
    fase_2_temperaturas_desordenadas(plantacoes)
    fase_2_1_temperaturas_ordenadas(plantacoes)
    fase_3_status(plantacoes)

    end_time = time.time()

    print(f"Tempo de execução: {end_time - start_time:.2f} segundos")


if __name__ == "__main__":
    main()

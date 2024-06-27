import threading
from client.src.sensores.temperatura import SensorTemperatura
from client.src.models import Temperatura
from typing import List

def gerar_leituras(quant: int, results: List[Temperatura], index: int):
    """
    Função que gera leituras de temperatura e as adiciona a uma lista compartilhada.

    :param quant: quantidade de leituras a serem geradas.
    :param results: lista compartilhada onde as leituras serão armazenadas.
    :param index: índice da thread (para depuração, se necessário).
    """
    sensor = SensorTemperatura()
    for _ in range(quant):
        temperatura = Temperatura(sensor.get_temperatura())
        results.append(temperatura)

def gerar_paralelo(quant: int, num_threads: int) -> List[Temperatura]:
    """
    Função que cria threads para gerar leituras de temperatura em paralelo.

    :param quant: quantidade total de leituras a serem geradas.
    :param num_threads: número de threads a serem usadas.
    :return: lista de leituras de temperatura.
    """
    threads = []
    results = []
    readings_per_thread = quant // num_threads

    for i in range(num_threads):
        thread = threading.Thread(target=gerar_leituras, args=(readings_per_thread, results, i))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    # Caso a divisão não seja exata, gerar o restante das leituras no thread principal
    remaining_readings = quant % num_threads
    if remaining_readings > 0:
        gerar_leituras(remaining_readings, results, num_threads)

    return results

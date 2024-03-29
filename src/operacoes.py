"""
Funções de operações
"""

"""
    Imprime as plantações
    :param data: lista de tuplas contendo plantação e temperaturas
    :return: None

    Complexidade: O(N)

    Esta função tem uma complexidade linear O(N)
    Pois tem apenas 1 loop para imprimir as plantações
"""


def imprimir_plantacao(data: list):
    for plantacao, _ in data:
        print(f"Plantacao: {plantacao}")


"""
    Imprime as plantações e suas respectivas temperaturas
    :param data: lista de tuplas contendo plantação e temperaturas
    :return: None

    Complexidade: O(N²)

    Esta função tem uma complexidade quadrática O(N²)
    Pois tem 2 loops aninhados:
    1º loop para pegar as plantações e temperaturas (na qual é uma lista)
    2º loop para capturar as temperaturas da lista
    E imprime o nome da plantação e a temperatura
"""


def imprimir_temperatura(data: list):
    for plantacao, temperaturas in data:
        print(f"Plantacao: {plantacao}")
        for temperatura in temperaturas:
            status_temperatura = verifica_temperatura(temperatura.get_value())
            print(f"Temperatura: {temperatura} - {status_temperatura}")
        print("\n")


def verifica_temperatura(temperatura: float) -> str:
    if temperatura < 20.0:
        return "Frio"
    elif temperatura >= 20.0 and temperatura <= 30.0:
        return "Ideal"
    else:
        return "Muito Quente"


"""
    Imprime o status das plantações, baseado na temperatura
    :param data: lista de tuplas contendo plantação e temperaturas
    :return: None

    Complexidade: O(N³)

    Esta função tem uma complexidade cubica O(N³) pois tem 3 loops aninhados
    Obtem todas as temperaturas de cada plantação,
    compara com os status mapeados
    E imprime o status da região baseado na temperatura

    Este algorítimo tem um custo de tempo e processamento alto,
    pode gerar um brute force, pois tem 3 loops aninhados e precisaria
    percorrer todos os dados.
    Dependendo da quantidade de plantações e leituras,
    o tempo de execução pode inviável
"""


def imprimir_status(data: list):
    TIPO_REGIAO = [
        {"nome": "congelando", "temperatura": 10.0},
        {"nome": "frio", "temperatura": 20.0},
        {"nome": "ideal", "temperatura": 30.0},
        {"nome": "quente", "temperatura": 40.0},
        {"nome": "muito quente", "temperatura": 50.0},
        {"nome": "queimando", "temperatura": 80.0},
    ]

    regioes = []

    for plantacao, temperaturas in data:
        print(f"Plantacao: {plantacao}")
        for temperatura in temperaturas:
            for regiao in TIPO_REGIAO:
                if temperatura.get_value() < regiao["temperatura"]:
                    regioes.append(regiao["nome"])
                    print(
                        f"Região: {regiao['nome']}",
                        f"- Temperatura: {temperatura.get_value()}",
                    )
                    break
        print("\n")


def orderna_temperatura(data: list):
    ...

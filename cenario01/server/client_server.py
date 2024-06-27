from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import uvicorn

app = FastAPI()

class Temperatura(BaseModel):
    value: float

class PlantacaoTemperatura(BaseModel):
    plantacao: str
    temperaturas: List[Temperatura]

data = []

@app.post("/sensores/")
def receive_data(plantacoes: List[PlantacaoTemperatura]):
    data.extend(plantacoes)
    return {"message": "Dados recebidos com sucesso"}

@app.get("/processar/")
def process_data():
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
    TIPO_REGIAO = [
        {"nome": "congelando", "temperatura": 10.0},
        {"nome": "frio", "temperatura": 20.0},
        {"nome": "ideal", "temperatura": 30.0},
        {"nome": "quente", "temperatura": 40.0},
        {"nome": "muito quente", "temperatura": 50.0},
        {"nome": "queimando", "temperatura": 80.0},
    ]

    regioes = []

    for plantacao_temperatura in data:
        plantacao = plantacao_temperatura.plantacao
        temperaturas = plantacao_temperatura.temperaturas

        for temperatura in temperaturas:
            for regiao in TIPO_REGIAO:
                if temperatura.value < regiao["temperatura"]:
                    regioes.append({
                        "plantacao": plantacao,
                        "regiao": regiao["nome"],
                        "temperatura": temperatura.value
                    })
                    break
    return regioes

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import uvicorn

app = FastAPI()

class ProcessedData(BaseModel):
    plantacao: str
    regiao: str
    temperatura: float

data = []

@app.post("/sensores/")
def receive_data(processed_data: List[ProcessedData]):
    data.extend(processed_data)
    return {"message": "Dados processados recebidos com sucesso"}

@app.get("/dados/")
def get_data():
    return data

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)

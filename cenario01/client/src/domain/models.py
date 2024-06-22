from abc import ABC, abstractmethod


class TemperaturaInterface(ABC):
    def __init__(self, value: float):
        self.value = value

    @abstractmethod
    def get_value(self) -> float:
        ...

    @abstractmethod
    def set_value(self, value: float) -> None:
        ...

    def __str__(self):
        return f"{self.value}°C"


class PlantacaoInterface(ABC):
    def __init__(self, nome: str):
        self.nome = nome

    def __str__(self):
        return f"{self.nome}"

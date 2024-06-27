from abc import ABC, abstractmethod


class ISensorTemperatura(ABC):
    @abstractmethod
    def get_temperatura(self) -> float:
        ...

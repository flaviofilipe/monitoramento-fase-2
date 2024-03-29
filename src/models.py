from src.domain.models import TemperaturaInterface, PlantacaoInterface


class Temperatura(TemperaturaInterface):
    def get_value(self) -> float:
        return self.value

    def set_value(self, value: float) -> None:
        self.value = value


class Plantacao(PlantacaoInterface):
    def monitoramento(self) -> float:
        return self.sensor.get_value()

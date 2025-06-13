from abc import ABC, abstractmethod

class Observador(ABC):
    @abstractmethod
    def atualizar(self, temperatura, humidade, pressao):
        pass

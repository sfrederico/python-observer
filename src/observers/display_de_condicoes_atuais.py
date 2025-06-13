from .observador import Observador


class DisplayDeCondicoesAtuais(Observador):
    def __init__(self):
        self.leituras = []

    def atualizar(self, temperatura, humidade, pressao):
        if len(self.leituras) >= 10:
            self.leituras.pop(0)
        self.leituras.append((temperatura, humidade, pressao))

    def ultima_leitura(self):
        return self.leituras[-1] if self.leituras else (None, None, None)

    def todas_leituras(self):
        return self.leituras

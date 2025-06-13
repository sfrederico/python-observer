from .observador import Observador


class DisplayEstatistico(Observador):
    def __init__(self):
        self.leituras = []

    def atualizar(self, temperatura, humidade, pressao):
        if len(self.leituras) >= 10:
            self.leituras.pop(0)
        self.leituras.append((temperatura, humidade, pressao))

    def media_temperatura(self):
        if not self.leituras:
            return None
        return sum(t for t, _, _ in self.leituras) / len(self.leituras)

    def media_humidade(self):
        if not self.leituras:
            return None
        return sum(h for _, h, _ in self.leituras) / len(self.leituras)

    def maxima_temperatura(self):
        if not self.leituras:
            return None
        return max(t for t, _, _ in self.leituras)

    def minima_temperatura(self):
        if not self.leituras:
            return None
        return min(t for t, _, _ in self.leituras)

from subjects.sujeito_observavel import SujeitoObservavel


class MonitorDeDadosDoClima(SujeitoObservavel):
    def __init__(self, equipamento):
        self.observadores = []
        self.temperatura = 0.0
        self.humidade = 0.0
        self.pressao = 0.0
        self.equipamento = equipamento

    def registra_observador(self, o):
        self.observadores.append(o)

    def remove_observador(self, o):
        if o in self.observadores:
            self.observadores.remove(o)

    def notifica_observadores(self):
        for observador in self.observadores:
            observador.atualizar(self.temperatura, self.humidade, self.pressao)

    def dados_mudaram(self):
        self.temperatura = self.equipamento.temperatura_atual
        self.humidade = self.equipamento.humidade_atual
        self.pressao = self.equipamento.pressao_atual
        self.notifica_observadores()

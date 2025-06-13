import random
import time


class EquipamentoDeMonitoramento:
    def __init__(self):
        self.gerador = random.Random()  # Gerador próprio da instância
        self.temperatura_atual = 0.0
        self.humidade_atual = 0.0
        self.pressao_atual = 0.0
        self.monitor_dados_clima = None

    def coletar(self):
        for _ in range(10):
            self.temperatura_atual = self.get_numero(0, 35)
            self.humidade_atual = self.get_numero(10, 100)
            self.pressao_atual = self.get_numero(900, 1100)
            if self.monitor_dados_clima:
                self.monitor_dados_clima.dados_mudaram()
            time.sleep(0.1)

    def get_numero(self, min_val, max_val):
        return round(self.gerador.uniform(min_val, max_val), 1)

class SujeitoObservavel:
    def registra_observador(self, o):
        raise NotImplementedError

    def remove_observador(self, o):
        raise NotImplementedError

    def notifica_observadores(self):
        raise NotImplementedError

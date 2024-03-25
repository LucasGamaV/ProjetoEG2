# Classe sujeito (subject)
class Sujeito:
    def __init__(self):
        self._observadores = []

    def registrar_observador(self, observador):
        self._observadores.append(observador)

    def remover_observador(self, observador):
        self._observadores.remove(observador)

    def notificar_observadores(self, dados):
        for observador in self._observadores:
            observador.atualizar(dados)

# Classe abstrata Observador
class Observador:
    def atualizar(self, dados):
        pass

# Classe para dados de benefícios
class DadosBeneficios:
    def __init__(self):
        self.dados = {}

    def atualizar_dados(self, novos_dados):
        self.dados = novos_dados

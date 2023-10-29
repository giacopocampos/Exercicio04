from Model.Veiculo import Veiculo


class Moto(Veiculo):
    def __init__(self, placa, valor):
        super().__init__(placa, valor, alugado=False, historico=[], cliente=None)

    def calcularAluguel(self, dias):
        valor_base = super().calcularAluguel(dias)
        if dias >= 30:
            return valor_base * 1.1
        else:
            return valor_base * 1.2


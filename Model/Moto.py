from Model.Veiculo import Veiculo


class Moto(Veiculo):
    def __init__(self):
        super().__init__()

    def calcularAluguel(self, dias):
        valor_base = super().calcularAluguel(dias)
        if dias >= 30:
            return valor_base * 1.1
        else:
            return valor_base * 1.2

    def listarMoto(self):
        print(f'Moto - PLACA: {self.getPlaca()}/ VALOR: {self.getValor()}/\n')
        

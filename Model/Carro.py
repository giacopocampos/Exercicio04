from Model.Veiculo import Veiculo


class Carro(Veiculo):
    def __init__(self, modelo, placa, valor):
        self.__modelo = modelo
        super().__init__(placa, valor, alugado=False, historico=[], cliente=None)
    
    def setModelo(self, modelo):
        self.__modelo = modelo
    
    def getModelo(self):
        return self.__modelo

    def calcularAluguel(self, dias):
        return super().calcularAluguel(dias)



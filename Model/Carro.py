from Model.Veiculo import Veiculo


class Carro(Veiculo):
    def __init__(self):
        self.__modelo = None
        super().__init__()
    
    def setModelo(self, modelo):
        self.__modelo = modelo
    
    def getModelo(self):
        return self.__modelo

    def calcularAluguel(self, dias):
        return super().calcularAluguel(dias)
    
    def listarCarro(self):
        print(f'Carro - MODELO: {self.getModelo()}/ PLACA: {self.getPlaca()}/ VALOR: {self.getValor()}/\n')




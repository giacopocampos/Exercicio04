import abc

class Veiculo(abc.ABC):

    def __init__(self, placa=None, valor=None, cliente=None, alugado=False, historico=[]):
        self.__placa = placa
        self.__valor = valor
        self.__alugado = alugado
        self.__historico = historico
        self.__cliente = cliente
    
    def setPlaca(self, placa):
        self.__placa = placa
    
    def getPlaca(self):
        return self.__placa
    
    def setValor(self, valor):
        self.__valor = valor
    
    def getValor(self):
        return self.__valor
    
    def setAlugado(self, alugado):
        self.__alugado = alugado
    
    def getAlugado(self):
        return self.__alugado
    
    def addHistorico(self, historico):
        self.__historico.append(historico)
    
    def getHistorico(self):
        return self.__historico
    
    def setCliente(self, cliente):
        self.__cliente = cliente

    def getCliente(self):
        return self.__cliente
    

    def alugar(self, cliente, placa, dias):
        if not self.__alugado:
            self.__alugado = True
            valor_total = self.calcularAluguel(dias)
            print(f'\n*Aluguel confirmado para o veículo de placa {placa}')
            self.__historico.append(f"|--Veiculo placa {placa} alugado pelo {cliente} por {dias} dias. Valor total: R${valor_total:.2f}--|")
            return True
        else:
            print(f"\n**Veiculo de placa {placa} não está disponível para aluguel. O cliente {cliente} terá que aguardar a devolução.")
            return False
    

    def devolver(self, placa):
        if self.__alugado:
            self.__alugado = False
            self.__historico.append(f"|--Devolução realizada para o veiculo de placa {placa}. Disponível para locação.--|")
            return True
        else:
            print(f"\n***Veiculo de placa {placa} nao está alugado. Nao e possivel devolver.")
            return False
    
    def removerHistorico(self, historico):
        if historico in self.__historico:
            self.__historico.remove(historico)

    def limparHistorico(self):
        return self.__historico.clear()

    def listarHistorico(self):
        for i in self.__historico:
            print(i)
    
    def calcularAluguel(self, dias):
        return dias * self.__valor
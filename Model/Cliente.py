class Cliente:
    def __int__(self):
        self.__nome = None
        self.__veiculos = []
    
    def setNome(self, nome):
        self.__nome = nome
    
    def getNome(self):
        return self.__nome
    
    def setVeiculos(self, veiculos):
        self.__veiculos = veiculos
    
    def getVeiculos(self):
        return self.__veiculos

    def addVeiculos(self, veiculos):
        self.__veiculos.append(veiculos)
    
    def remove_veiculos(self, veiculos):
        if veiculos in self.__veiculos:
            self.__veiculos.remove(veiculos)
    
    def listarCliente(self):
        print('Nome do Cliente: ' + self.getNome())

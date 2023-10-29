from Model.Carro import Carro
from Model.Moto import Moto
from Model.Cliente import Cliente


#CLIENTES
cliente1 = Cliente()
cliente1.setNome('Marco')
cliente1.listarCliente()

cliente2 = Cliente()
cliente2.setNome('Antonio')
cliente2.listarCliente()
      
#VEÍCULOS DA LOCAÇÃO
carro1 = Carro('Celta', 'ABC123', 100)

carro2 = Carro('Celta', 'XYZ123', 80)

moto1 = Moto('MOT123', 40)
    
moto2 = Moto('MOT234', 50)

# LOCAÇÃO
print('\n*************************INFORMAÇÕES LOCAÇÃO*************************\n')
carro1.alugar(cliente1.getNome(), carro1.getPlaca(),  5)

moto1.alugar(cliente1.getNome(), moto1.getPlaca(), 5)

carro2.alugar(cliente2.getNome(), carro2.getPlaca(), 5)

moto2.alugar(cliente2.getNome(), moto2.getPlaca(), 5)

# TENTAR ALUGAR VEÍCULO JÁ LOCADO

carro1.alugar(cliente2.getNome(), carro1.getPlaca(),  5)

moto1.alugar(cliente2.getNome(), moto1.getPlaca(), 5)

carro2.alugar(cliente1.getNome(), carro2.getPlaca(), 5)

moto2.alugar(cliente1.getNome(), moto2.getPlaca(), 5)

#DEVOLUÇÃO
carro1.devolver(carro1.getPlaca())

moto1.devolver(moto1.getPlaca())

carro2.devolver(carro2.getPlaca())

moto2.devolver(moto2.getPlaca())

# TENTAR DEVOLVER VEÍCULO JÁ ENTREGUE

carro1.devolver(carro1.getPlaca())

moto1.devolver(moto1.getPlaca())

carro2.devolver(carro2.getPlaca())

moto2.devolver(moto2.getPlaca())

#HISTÓRICO
print('\n*************************Histórico*************************\n')
print("\nHistorico do veículo de placa" + carro1.getPlaca())
carro1.listarHistorico()

print("\nHistorico do veículo de placa" + moto1.getPlaca())
moto1.listarHistorico()

print("\nHistorico do veículo de placa" + carro2.getPlaca())
carro2.listarHistorico()

print("\nHistorico do veículo de placa" + moto2.getPlaca())
moto2.listarHistorico()
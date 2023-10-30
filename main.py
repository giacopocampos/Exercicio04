from Model.Carro import Carro
from Model.Moto import Moto
from Model.Cliente import Cliente

def principal():
    #CLIENTES
    print('\n*************************CLIENTES*************************\n')
    cliente1 = Cliente()
    cliente1.setNome('Marco\n')
    cliente1.listarCliente()

    cliente2 = Cliente()
    cliente2.setNome('Antonio')
    cliente2.listarCliente()
    
    print('\n*************************VEÍCULOS*************************\n')
    #VEÍCULOS DA LOCAÇÃO
    carro1 = Carro()
    carro1.setModelo('Celta')
    carro1.setPlaca('ABC123')
    carro1.setValor(100)
    carro1.listarCarro()

    carro2 = Carro()
    carro2.setModelo('Gol')
    carro2.setPlaca('XYZ123')
    carro2.setValor(80)
    carro2.listarCarro()

    moto1 = Moto()
    moto1.setPlaca('MOT123')
    moto1.setValor(40)
    moto1.listarMoto()

    moto2 = Moto()
    moto2.setPlaca('MOT234')
    moto2.setValor(50)
    moto2.listarMoto()

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

if __name__ == '__main__':
    principal()
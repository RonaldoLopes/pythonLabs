from abc import ABC, abstractmethod

class Veiculo(ABC):
    @abstractmethod
    def buscar_clientes(self) -> None: pass

class CarroLuxo(Veiculo):
    def buscar_clientes(self) -> None:
        print('Carro de luxo está buscando o cliente')


class CarroPopular(Veiculo):
    def buscar_clientes(self) -> None:
        print('Carro popular está buscando o cliente')


class Moto(Veiculo):
    def buscar_clientes(self) -> None:
        print('Moto popular está buscando o cliente')


class VeiculoFactory:
    @staticmethod
    def get_carro(tipo: str) -> Veiculo:
        if tipo == 'luxo':
            return CarroLuxo()
        if tipo == 'popular':
            return CarroPopular()
        if tipo == 'moto':
            return Moto()
        assert 0, 'Veiculo não existe'

    
if __name__ == "__main__":
    from random import choice
    carros_disponiveis = ['luxo', 'popular', 'moto']

    for i in range(10):
        carro = VeiculoFactory.get_carro(choice(carros_disponiveis))
        carro.buscar_clientes()

"""
Strategy é um padrão de projeto comportamental que tem
a intenção de definir uma familia de algoritmo,
encapsular cada uma delas e torná-las intercambiáveis.
Strategy permite que o algoritmo varie independentemente
dos clientes que o utilizam.

Principio do aberto/fechado (Open/closed principle)
Entidades devem ser abertas por extensão, mas fechadas para modificação
"""
from __future__ import annotations
from abc import ABC, abstractmethod


class Order:
    def __init__(self, total: float, discount: DiscountStrategy):
        self._total = total
        self._discount = discount

    @property
    def total(self):
        return self._total

    @property
    def total_with_discount(self):
        return self._discount.calculate(self.total)


class DiscountStrategy(ABC):
    @abstractmethod
    def calculate(self, value: float) -> float: pass


class TwentyPercent(DiscountStrategy):
    def calculate(self, value: float) -> float:
        return value - (value * 0.2)


class FifityPercent(DiscountStrategy):
    def calculate(self, value: float) -> float:
        return value - (value * 0.5)


class NoDiscount(DiscountStrategy):
    def calculate(self, value: float) -> float:
        return value


if __name__ == "__main__":
    twenty_percent = TwentyPercent()
    fifty_percent = FifityPercent()
    no_discount = NoDiscount()

    order = Order(1000, twenty_percent)
    print(order.total, order.total_with_discount)

    order = Order(1000, fifty_percent)
    print(order.total, order.total_with_discount)

    order = Order(1000, no_discount)
    print(order.total, order.total_with_discount)

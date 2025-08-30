from abc import ABC, abstractmethod
from typing import Any


class BaseProduct(ABC):
    """ Abstract class for class Product """

    @classmethod
    @abstractmethod
    def new_product(cls) -> Any:
        pass


    @property
    @abstractmethod
    def price(self) -> float:
        pass


    @price.setter
    @abstractmethod
    def price(self, price: float) -> None:
        pass


class BaseOrder(ABC):
    """ Abstract class for classes Order and Category """

    @property
    @abstractmethod
    def products(self) -> str:
        pass
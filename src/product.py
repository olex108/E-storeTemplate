from typing import Any
from src.abstract_classes import BaseProduct
from src.mixin_classes import ProductMixin


class Product(BaseProduct, ProductMixin):
    """
    Class Product descriptions name, short description, price and quantity of product.
    Class describe methods for add new products, addition products, change price and others
    """

    name: str
    description: str
    price: float
    quantity: int

    products_list: list = []

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """
        Class initializer

        :param name: Name of the product
        :param description: Description of the product
        :param price: Price of the product
        :param quantity: Quantity of the product
        """

        self.name = name
        self.description = description
        self.__price = price
        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        else:
            self.quantity = quantity

        Product.products_list.append(self)

        super().__init__()

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: Any) -> Any:
        """
        Dander method to add products include check if products are in one class

        :return: sum of price oll quantity of products
        """

        if type(self) is type(other):
            return round(self.price * self.quantity + other.price * other.quantity, 2)
        else:
            raise TypeError("Different product classes")

    @classmethod
    def new_product(cls, product_in_dict: dict) -> Any:
        """
        Create new product from given dictionary if product_in_dict describe as class create new product

        If product exist in product list, method add quantity to product and change product price if it is bigger
        than previous price.

        If user try to add product with zero quantity method raise ValueError

        :param product_in_dict: description of the product in dict
        :return: new object of product class
        """

        for product in cls.products_list:

            if product.name == product_in_dict["name"]:
                product.description = product_in_dict["description"]
                product.__price = (
                    product_in_dict["price"] if product_in_dict["price"] > product.__price else product.price
                )
                product.quantity += product_in_dict["quantity"]

                return product

        name = product_in_dict["name"]
        description = product_in_dict["description"]
        __price = product_in_dict["price"]

        if product_in_dict["quantity"] == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        else:
            quantity = product_in_dict["quantity"]

        return cls(name, description, __price, quantity)

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, price: float) -> None:
        if price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif price < self.__price:
            answer = input("Вы понижаете стоимость товара! Подтвердить?(y/n): ")
            if answer.lower() == "y":
                self.__price = price
        else:
            self.__price = price


class Smartphone(Product):
    """
    Class Smartphone descriptions name, short description, price and quantity of product,
    efficiency, model, memory, color
    """

    efficiency: float
    model: str
    memory: int
    color: str

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ) -> None:
        """Class initializer"""

        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """
    Class Smartphone descriptions name, short description, price and quantity of product,
    country, germination_period, color
    """

    country: str
    germination_period: str
    color: str

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ) -> None:
        """Class initializer"""

        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color


# if __name__ == "__main__":
#     pass
# prod_1 = Product(name="Lemon", description="Yellow lemon", price=6.40, quantity=600)
# print(prod_1.name)
#
# print(Product.new_product({"name": "Банан", "description": "Yellow lemon", "price": 6.40, "quantity": 60}).name)
#
# print(Product.products_list)
#
# print(Product.new_product({"name": "Банан", "description": "Yellow lemon", "price": 7.40, "quantity": 60}).price)
#
# print(Product.products_list[1].price)
# Product.products_list[1].price = 7.2
#
# print(Product.products_list[1].price)
#
# print(Product.new_product({"name": "Банан", "description": "Yellow lemon", "price": 7.40, "quantity": 60}).price)
#
# print(Product.products_list)
# # print(prod_2.name)
# # print(prod_2.description)
# # print(prod_2.price)

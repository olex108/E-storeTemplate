from typing import Any


class Product:
    """
    Class Product descriptions name, short description, price and quantity of product
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
        self.quantity = quantity

        Product.products_list.append(self)

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: Any) -> Any:
        return round(self.price * self.quantity + other.price * other.quantity, 2)

    @classmethod
    def new_product(cls, product_in_dict: dict) -> Any:

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

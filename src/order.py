from src.product import Product
from src.abstract_classes import BaseOrder
from src.exception_classes import ZeroProductQuantityError


class Order(BaseOrder):
    """
    The class describes product, quantity and price in order
    """

    product: Product
    quantity: int

    def __init__(self, product: Product, quantity: int) -> None:
        """
        Initialization method
        :param product: Product instance
        :param quantity: Quantity
        total_price: Total price

        """

        self.product = product
        self.quantity = self.check_quantity(quantity)
        self.total_price = round(product.price * self.quantity, 2)

    def __str__(self) -> str:
        return f"{self.product.name}, quantity: {self.quantity}, total price: {self.total_price}"

    def check_quantity(self, quantity: int) -> int:

        try:
            if self.product.quantity == 0:
                raise ZeroProductQuantityError("Нельзя добавить товар с количеством 0")
        except ZeroProductQuantityError as e:
            print(str(e))
        else:
            if quantity <= self.product.quantity:
                self.product.quantity -= quantity
                print("Товар успешно добавлен")
            else:
                print(f"Max quantity of is {self.product.quantity}")
                quantity = self.product.quantity
                self.product.quantity = 0
        finally:
            print("Проверка исключения прошла успешно")

        return quantity

    @property
    def products(self) -> str:
        return f"{self.product.name}, quantity: {self.quantity}, total price: {self.total_price}"

from src.product import Product
from src.abstract_classes import BaseOrder


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
        if quantity <= self.product.quantity:
            self.product.quantity -= quantity
            return quantity
        else:
            print(f"Max quantity of is {self.product.quantity}")
            max_quantity = self.product.quantity
            self.product.quantity = 0
            return max_quantity

    @property
    def products(self) -> str:
        return f"{self.product.name}, quantity: {self.quantity}, total price: {self.total_price}"

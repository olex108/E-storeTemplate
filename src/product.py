class Product:
    """
    Class Product descriptions name, short description, price and quantity of product
    """

    name: str
    description: str
    price: float
    quantity: int

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
        self.price = price
        self.quantity = quantity

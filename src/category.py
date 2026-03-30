from src.abstract_classes import BaseOrder

from typing import List

from src.product import Product


class Category(BaseOrder):
    """
    The class describes the name, short description and list of products of the category
    Class describe method for add product object
    """

    name: str
    description: str
    products: List[Product]

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: List[Product]) -> None:
        """
        Class initializer

        :param name: Name of the category
        :param description: Description of the category
        :param products: List of products of the category
        """

        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self) -> str:
        return f"{self.name}, количество продуктов: {sum(product.quantity for product in self.__products)} шт."

    @property
    def products(self) -> str:
        return "\n".join(str(product) for product in self.__products)

    @property
    def products_list(self) -> List[Product]:
        return self.__products

    def add_product(self, product: Product) -> None:
        """Method to add new product to the category, include check if user add product object"""

        if isinstance(product, Product):
            if product not in self.__products:
                self.__products.append(product)
                Category.product_count += 1
        else:
            raise TypeError("You add not a Product")

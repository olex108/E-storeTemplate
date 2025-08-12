from typing import List

from src.product import Product


class Category:
    """
    The class describes the name, short description and list of products of the category
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
        self.products = products

        Category.category_count += 1
        Category.product_count += len(products)

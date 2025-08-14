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
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    @property
    def products(self) -> str:
        products_in_str = ""
        for product in self.__products:
            products_in_str = (
                products_in_str + f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
            )
        return products_in_str

    def add_product(self, product: Product) -> None:
        if product not in self.__products:
            self.__products.append(product)
            Category.product_count += 1

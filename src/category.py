from src.abstract_classes import BaseOrder

from typing import List

from src.product import Product
from src.exception_classes import ZeroProductQuantityError


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
        """
        Method to add new product to the category.
        Include checking:
         - if user add product object raise TypeError
         - If quantity of product is 0 raise error
        """

        if isinstance(product, Product):
            try:
                if product.quantity == 0:
                    raise ZeroProductQuantityError("Нельзя добавить товар с количеством 0")
            except ZeroProductQuantityError as e:
                print(str(e))
            else:
                if product not in self.__products:
                    self.__products.append(product)
                    Category.product_count += 1
                    print("Товар успешно добавлен")
                else:
                    print("Товар уже существует")
            finally:
                print("Проверка исключения прошла успешно")
        else:
            raise TypeError("You add not a Product")

    def middle_price(self) -> float:
        """
        Method to get average price for products in category,
        if there are no products in category return 0

        :return: Average price for products in category
        """

        try:
            return round(sum(product.price for product in self.__products) / len(self.__products), 2)
        except ZeroDivisionError:
            return 0

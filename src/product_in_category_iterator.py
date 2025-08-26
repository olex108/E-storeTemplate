from typing import Any, Self

from src.category import Category


class ProductInCategoryIterator:
    """Class of Iterator for list od products in category"""

    def __init__(self, category_obj: Category) -> None:

        self.category_obj = category_obj

    def __iter__(self) -> Self:

        self.index = -1
        return self

    def __next__(self) -> Any:
        if self.index < len(self.category_obj.products_list) - 1:
            self.index += 1
            return self.category_obj.products_list[self.index]
        else:
            raise StopIteration


# if __name__ == "__main__":
#     product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
#     product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
#     product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
#
#     category1 = Category(
#         "Смартфоны",
#         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
#         [product1, product2, product3]
#     )
#
#     print(type(category1))
#
#     iter_cat = ProductInCategoryIterator(category1)
#
#     print(type(iter_cat))
#
#     iter(iter_cat)
#     print(next(iter_cat))
#     print(next(iter_cat))
#     print(next(iter_cat))
#     #
#     for product in iter_cat:
#         print(product)

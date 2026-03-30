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

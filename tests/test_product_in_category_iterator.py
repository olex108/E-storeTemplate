import pytest

from src.category import Category
from src.product_in_category_iterator import ProductInCategoryIterator


def test_product_in_category_iterator(category_fruits: Category) -> None:
    iter_1 = ProductInCategoryIterator(category_fruits)

    iter(iter_1)

    assert str(next(iter_1)) == "Apple, 5.99 руб. Остаток: 1000 шт."
    assert str(next(iter_1)) == "Lemon, 6.4 руб. Остаток: 600 шт."

    with pytest.raises(StopIteration):
        next(iter_1)

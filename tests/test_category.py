import pytest

from src.category import Category, Product


def test_category_init(category_berries: Category, category_fruits: Category) -> None:

    assert category_berries.name == "Berries"
    assert category_berries.description == "Different berries"

    assert category_berries.category_count == 2
    assert category_fruits.category_count == 2
    assert category_berries.product_count == 3


def test_category_str(category_berries: Category) -> None:
    assert str(category_berries) == "Berries, количество продуктов: 1000 шт."


def test_category_getter_products(category_berries: Category, product_blackberry: Product) -> None:
    assert category_berries.name == "Berries"
    assert category_berries.description == "Different berries"

    assert category_berries.products == "Strawberry, 12.3 руб. Остаток: 1000 шт."

    # Add new product in category
    category_berries.add_product(product_blackberry)

    assert category_berries.products == (
        """Strawberry, 12.3 руб. Остаток: 1000 шт.
Blackberry, 1.4 руб. Остаток: 1200 шт."""
    )

    # Test add same product in category
    category_berries.add_product(product_blackberry)

    assert category_berries.products == (
        """Strawberry, 12.3 руб. Остаток: 1000 шт.
Blackberry, 1.4 руб. Остаток: 1200 шт."""
    )


def test_category_getter_products_list(category_fruits: Category) -> None:
    assert type(category_fruits.products_list) is list


def test_try_add_product_in_category(category_berries: Category, product_blackberry: Product) -> None:
    category_berries.add_product(product_blackberry)

    with pytest.raises(TypeError):
        category_berries.add_product("String object")


def test_middle_price(category_fruits: Category) -> None:
    assert category_fruits.middle_price() == 6.20

    cat_1 = Category(
        name="Fruits",
        description="Different fruits",
        products=[]
    )

    assert cat_1.middle_price() == 0
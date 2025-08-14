from src.category import Category, Product


def test_category_init(category_berries: Category, category_fruits: Category) -> None:

    assert category_berries.name == "Berries"
    assert category_berries.description == "Different berries"

    assert category_berries.category_count == 2
    assert category_fruits.category_count == 2

    assert category_berries.product_count == 3


def test_category_getter(category_berries: Category, product_blackberry: Product) -> None:
    assert category_berries.name == "Berries"
    assert category_berries.description == "Different berries"

    assert category_berries.products == "Strawberry, 12.3 руб. Остаток: 1000 шт.\n"

    # Add new product in category
    category_berries.add_product(product_blackberry)

    assert category_berries.products == (
        "Strawberry, 12.3 руб. Остаток: 1000 шт.\n" "Blackberry, 1.4 руб. Остаток: 1200 шт.\n"
    )

    # Test add same product in category
    category_berries.add_product(product_blackberry)

    assert category_berries.products == (
        "Strawberry, 12.3 руб. Остаток: 1000 шт.\n" "Blackberry, 1.4 руб. Остаток: 1200 шт.\n"
    )

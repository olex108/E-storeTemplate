from src.category import Category


def test_category_init(category_berries: Category, category_fruits: Category) -> None:
    assert category_berries.name == "Berries"
    assert category_berries.description == "Different berries"
    assert len(category_berries.products) == 1
    assert len(category_fruits.products) == 2

    assert category_berries.category_count == 2
    assert category_fruits.category_count == 2

    assert category_berries.product_count == 3

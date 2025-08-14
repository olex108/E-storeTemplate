import os
from unittest.mock import Mock, patch

from src.utils import create_category_objects_from_data, load_data_from_json


@patch("json.load")
def test_load_data_from_json(mock_json: Mock, categories_list: list) -> None:
    mock_json.return_value = categories_list
    result = categories_list
    path_to_file = os.path.join("data", "products.json")
    assert load_data_from_json(path_to_file) == result


def test_load_data_from_json_error() -> None:
    assert load_data_from_json("") == []


def test_create_category_objects_from_data(categories_list: list) -> None:

    category_objects_list = create_category_objects_from_data(categories_list)

    # Test categories objects
    assert category_objects_list[0].name == "Смартфоны"
    assert category_objects_list[0].description == "Смартфоны, как средство не только коммуникации"
    assert category_objects_list[1].description == "Современный телевизор, который позволяет наслаждаться просмотром"
    assert category_objects_list[1].name == "Телевизоры"

    # Test products objects
    assert category_objects_list[0].products == (
        "Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
        "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n"
    )
    assert category_objects_list[1].products == '55" QLED 4K, 123000.0 руб. Остаток: 7 шт.\n'

    # Test Category counters
    assert category_objects_list[0].category_count == 2
    assert category_objects_list[1].category_count == 2
    assert category_objects_list[1].product_count == 4

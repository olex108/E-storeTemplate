import json
from typing import Any, List

from src.category import Category
from src.product import Product


def load_data_from_json(path_to_json: str) -> Any:
    """
    Function to load data from json file

    :param path_to_json: Path to json file
    :return: List of dicts
    """

    try:
        with open(path_to_json, "r", encoding="utf-8") as json_file:
            file_data = json.load(json_file)
    except FileNotFoundError:
        file_data = []

    return file_data


def create_category_objects_from_data(data: List[dict]) -> List[Category]:
    """
    Function to create category objects from data, which include list of Products objects

    :param data: List of dicts with attributes of Category
    :return: List of Category objects
    """

    category_objects_list = []
    for item in data:
        category_objects_list.append(
            Category(
                name=item["name"],
                description=item["description"],
                products=[Product.new_product(i) for i in item["products"]],
            )
        )

    return category_objects_list

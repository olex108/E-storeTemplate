import json
from typing import List

import pytest

from src.category import Category
from src.product import Product


@pytest.fixture(autouse=True)
def reset_category_counters() -> None:
    Product.products_list.clear()
    Category.category_count = 0
    Category.product_count = 0


# Fixtures to create object of classes Category and Product
@pytest.fixture
def product_apple() -> Product:
    return Product(name="Apple", description="Big red apple", price=5.99, quantity=1000)


@pytest.fixture
def product_lemon() -> Product:
    return Product(name="Lemon", description="Yellow lemon", price=6.40, quantity=600)


@pytest.fixture
def product_blackberry() -> Product:
    return Product(name="Blackberry", description="black berry", price=1.40, quantity=1200)


@pytest.fixture
def category_fruits() -> Category:
    return Category(
        name="Fruits",
        description="Different fruits",
        products=[
            Product(name="Apple", description="Big red apple", price=5.99, quantity=1000),
            Product(name="Lemon", description="Yellow lemon", price=6.40, quantity=600),
        ],
    )


@pytest.fixture
def category_berries() -> Category:
    return Category(
        name="Berries",
        description="Different berries",
        products=[
            Product(name="Strawberry", description="Big red strawberry", price=12.30, quantity=1000),
        ],
    )


# Fixtures to create json data and lists of data
@pytest.fixture
def categories_list() -> List[dict]:
    return [
        {
            "name": "Смартфоны",
            "description": "Смартфоны, как средство не только коммуникации",
            "products": [
                {
                    "name": "Samsung Galaxy C23 Ultra",
                    "description": "256GB, Серый цвет, 200MP камера",
                    "price": 180000.0,
                    "quantity": 5,
                },
                {"name": "Iphone 15", "description": "512GB, Gray space", "price": 210000.0, "quantity": 8},
                {"name": "Xiaomi Redmi Note 11", "description": "1024GB, Синий", "price": 31000.0, "quantity": 14},
            ],
        },
        {
            "name": "Телевизоры",
            "description": "Современный телевизор, который позволяет наслаждаться просмотром",
            "products": [
                {"name": '55" QLED 4K', "description": "Фоновая подсветка", "price": 123000.0, "quantity": 7}
            ],
        },
    ]


@pytest.fixture
def categories_list_json_data() -> str:
    return json.dumps(
        [
            {
                "name": "Смартфоны",
                "description": "Смартфоны, как средство не только коммуникации",
                "products": [
                    {
                        "name": "Samsung Galaxy C23 Ultra",
                        "description": "256GB, Серый цвет, 200MP камера",
                        "price": 180000.0,
                        "quantity": 5,
                    },
                    {"name": "Iphone 15", "description": "512GB, Gray space", "price": 210000.0, "quantity": 8},
                    {"name": "Xiaomi Redmi Note 11", "description": "1024GB, Синий", "price": 31000.0, "quantity": 14},
                ],
            },
            {
                "name": "Телевизоры",
                "description": "Современный телевизор, который позволяет наслаждаться просмотром",
                "products": [
                    {"name": '55" QLED 4K', "description": "Фоновая подсветка", "price": 123000.0, "quantity": 7}
                ],
            },
        ],
        ensure_ascii=False,
    )


# @pytest.fixture
# def category_fruits_iterator() -> ProductInCategoryIterator:
#     return ProductInCategoryIterator(
#         name="Fruits",
#         description="Different fruits",
#         products=[
#             Product(name="Apple", description="Big red apple", price=5.99, quantity=1000),
#             Product(name="Lemon", description="Yellow lemon", price=6.40, quantity=600),
#         ],
#     )

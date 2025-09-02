import pytest
from _pytest.capture import CaptureFixture

from src.product import Product


def test_product_init(product_apple: Product, product_lemon: Product) -> None:
    assert product_apple.name == "Apple"
    assert product_apple.description == "Big red apple"
    assert product_apple.price == 5.99
    assert product_apple.quantity == 1000
    assert product_lemon.name == "Lemon"
    assert product_lemon.description == "Yellow lemon"
    assert product_lemon.price == 6.40
    assert product_lemon.quantity == 600

    # Raise ValueError when try to init object with zero quantity
    with pytest.raises(ValueError):
        Product(name="Blackberry", description="black berry", price=1.40, quantity=0)


def test_product_str(product_apple: Product) -> None:
    assert str(product_apple) == "Apple, 5.99 руб. Остаток: 1000 шт."


def test_product_add(product_apple: Product, product_lemon: Product) -> None:
    assert product_apple + product_lemon == 9830.00


def test_product_new_product(categories_list: list, product_zero_quantity_dict) -> None:
    # Test initialisation with class method
    prod_1 = Product.new_product(categories_list[0]["products"][0])

    assert prod_1.name == "Samsung Galaxy C23 Ultra"
    assert prod_1.price == 180000.0
    assert prod_1.quantity == 5

    # Test add product with same name
    Product.new_product(categories_list[0]["products"][0])

    assert prod_1.quantity == 10
    assert Product.products_list == [prod_1]

    # Test add product with zero quantity
    with pytest.raises(ValueError):
        Product.new_product(product_zero_quantity_dict)



def test_getter_setter_product(product_apple: Product) -> None:
    prod_1 = product_apple
    assert prod_1.price == 5.99

    prod_1.price = 6.40

    assert prod_1.price == 6.40


def test_setter_product_zero_price(product_apple: Product, capsys: CaptureFixture[str]) -> None:
    prod_1 = product_apple
    prod_1.price = 0
    capture = capsys.readouterr()
    assert capture.out == "Цена не должна быть нулевая или отрицательная\n"


def test_smartphone_initialisation(smartphone_list: list) -> None:
    assert smartphone_list[0].name == "Xiaomi Redmi Note 11"
    assert smartphone_list[0].description == "1024GB, Синий"


def test_grass_initialisation(grass_list: list) -> None:
    assert grass_list[0].name == "Газонная трава"
    assert grass_list[0].description == "Элитная трава для газона"


def test_add_products(smartphone_list: list, grass_list: list) -> None:
    assert (smartphone_list[0] + smartphone_list[1]) == 2114000.0
    with pytest.raises(TypeError):
        sum_error = smartphone_list[0] + grass_list[1]

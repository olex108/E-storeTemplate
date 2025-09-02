from src.product import Product
from src.order import Order


def test_order(product_blackberry: Product) -> None:
    order_1 = Order(product_blackberry, 20)
    assert order_1.products == "Blackberry, quantity: 20, total price: 28.0"
    assert product_blackberry.quantity == 1180


def test_order_max_quantity(product_blackberry: Product) -> None:
    order_1 = Order(product_blackberry, 1400)
    assert order_1.products == "Blackberry, quantity: 1200, total price: 1680.0"
    assert product_blackberry.quantity == 0

def test_order_printing(capsys, product_zero_quantity: Product) -> None:

    Order(product_zero_quantity, 0)
    capture = capsys.readouterr()
    assert capture.out.split("\n")[-3] == "Нельзя добавить товар с количеством 0"
    assert capture.out.split("\n")[-2] == "Проверка исключения прошла успешно"

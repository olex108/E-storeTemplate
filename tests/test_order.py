from src.order import Order

def test_order(product_blackberry):
    order_1= Order(product_blackberry, 20)
    assert order_1.products == "Blackberry, quantity: 20, total price: 28.0"
    assert product_blackberry.quantity == 1180

def test_order_max_quantity(product_blackberry):
    order_1= Order(product_blackberry, 1400)
    assert order_1.products == "Blackberry, quantity: 1200, total price: 1680.0"
    assert product_blackberry.quantity == 0
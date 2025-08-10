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

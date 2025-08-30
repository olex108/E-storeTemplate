from pyexpat.errors import messages

from src.product import Product

def test_print_mixin_product(capsys):
    Product(name="Blackberry", description="black berry", price=1.40, quantity=1200)
    message = capsys.readouterr()
    assert message.out == 'Product(\'Blackberry\', \'black berry\', \'1.4\', "1200\')\n'
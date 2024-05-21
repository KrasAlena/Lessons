import pytest
from Ex_3 import POSSystem, Product


@pytest.fixture
def pos_system():
    return POSSystem()


def test_pos_system(pos_system):
    # Adds products to the system
    pos_system.add_product(2, 'Product A', 20.0)
    pos_system.add_product(3, 'Product B', 30.9)

    # Get a list of all product
    pos_system.get_all_products()

    # Add products to the cart
    pos_system.add_to_cart(2, 20)

    # View the cart
    pos_system.view_cart()

    # Checkout
    total = pos_system.checkout()
    assert total == 400


def test_simple_shopping_scenario(pos_system):
    # Add products
    pos_system.add_product(1, 'Product A', 10.0)
    pos_system.add_product(2, 'Product B', 20.0)

    # Add products to cart
    pos_system.add_to_cart(1, 2)
    pos_system.add_to_cart(2, 1)

    # View cart
    total_price = pos_system.view_cart()
    assert total_price == 40.0

    # Remove a product from cart
    pos_system.remove_from_cart(1, 1)
    total_price = pos_system.view_cart()
    assert total_price == 30.0

    # Checkout
    total_price = pos_system.checkout()
    assert total_price == 30.0







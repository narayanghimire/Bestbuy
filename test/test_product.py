import pytest
from products import Product


def test_create_normal_product():
    product = Product("MacBook Air M2", price=1450, quantity=100)
    assert product._name == "MacBook Air M2"
    assert product.get_quantity() == 100
    assert product.is_active() == True


def test_create_product_with_empty_name():
    with pytest.raises(ValueError):
        Product("", price=1450, quantity=100)


def test_create_product_with_negative_price():
    with pytest.raises(ValueError):
        Product("MacBook Air M2", price=-10, quantity=100)


def test_create_product_with_negative_quantity():
    with pytest.raises(ValueError):
        Product("MacBook Air M2", price=-100, quantity=-100)


def test_product_becomes_inactive_when_quantity_zero():
    product = Product("MacBook Air M2", price=1450, quantity=1)
    product.buy(1)
    assert product.get_quantity() == 0
    assert product.is_active() == False


def test_product_purchase_modifies_quantity_and_returns_right_output():
    product = Product("MacBook Air M2", price=1450, quantity=20)
    total_price = product.buy(3)
    assert total_price == 1450 * 3
    assert product.get_quantity() == 17


def test_buying_more_than_available_quantity_throws_exception():
    product = Product("MacBook Air M2", price=1450, quantity=100)
    with pytest.raises(ValueError):
        product.buy(200)

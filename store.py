from typing import List, Tuple
from products import Product


class Store:
    def __init__(self, products: List[Product]):
        self._products = products

    def add_product(self, product: Product):
        self._products.append(product)

    def remove_product(self, product: Product):
        if product in self._products:
            self._products.remove(product)

    def get_total_quantity(self) -> int:
        return sum(product.get_quantity() for product in self._products)

    def get_all_products(self) -> List[Product]:
        return [product for product in self._products if product.is_active()]

    def order(self, shopping_list: List[Tuple[Product, int]]) -> float:
        total_price = 0.0
        for product, quantity in shopping_list:
            if not product.is_active():
                raise Exception(f"Product '{product.get_name()}' is not active.")
            if quantity <= 0:
                raise ValueError("Quantity must be positive.")

            if quantity > product.get_quantity():
                raise ValueError(f"Not enough stock for product '{product.get_name()}'.")

            total_price += product.buy(quantity)
        return total_price

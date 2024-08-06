from typing import List, Tuple
from products import Product


class Store:
    """
    shows a store can holds multiple products.
    """
    def __init__(self, products: List[Product]):
        """
            Initializes the Store object.
        """
        self._products = products

    def add_product(self, product: Product):
        """
            Adds a product to the store.
        """
        self._products.append(product)

    def remove_product(self, product: Product):
        """
         Removes a product from the store.
        """
        self._products.remove(product)

    def get_total_quantity(self) -> int:
        """
         Gets the total quantity of items in the store.
        """
        return sum(product.get_quantity() for product in self._products)

    def get_all_products(self) -> List[Product]:
        """
         Gets  all the products in the store.
        """
        return [product for product in self._products if product.is_active()]

    def order(self, shopping_list: List[Tuple[Product, int]]) -> float:
        """
         order the products from the store.
        """
        total_price = 0.0
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)
        return total_price

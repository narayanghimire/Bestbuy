class Product:
    """
    Show a different type of product available in the store.
    """

    def __init__(self, name: str, price: float, quantity: int):
        """
         Initializes the Product  object via constructor.
         Throws an exception if wrong value  of price and quantity is given
        """
        if not name:
            raise ValueError("Name cannot be empty.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self._name = name
        self._price = price
        self._quantity = quantity
        self._active = True

    def get_quantity(self) -> int:
        """
        Getter for quantity & returns The quantity of the product.
        """
        return self._quantity

    def set_quantity(self, quantity: int):
        """
        If quantity reaches 0, deactivates the product.
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self._quantity = quantity
        if self._quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        """
       Checks if the product is active & returns True or False.
        """
        return self._active

    def activate(self):
        """
        Activates the product.
        """
        self._active = True

    def deactivate(self):
        """
        Deactivates the product.
        """
        self._active = False

    def show(self) -> str:
        """
        show the product as a string
        """
        return f"{self._name}, Price: {self._price}, Quantity: {self._quantity}"

    def buy(self, quantity: int) -> float:
        """
            Buys a given quantity of the product.
         """
        if not self._active:
            raise Exception("Product is not active.")
        if quantity <= 0:
            raise ValueError("Quantity to buy must be positive.")
        if quantity > self._quantity:
            raise ValueError("Not enough stock to complete the purchase.")

        total_price = quantity * self._price
        self.set_quantity(self._quantity - quantity)
        return total_price


class NonStockedProduct(Product):
    """
        Represents a product that is not physically stocked.
     """

    def __init__(self, name: str, price: float):
        super().__init__(name, price, quantity=0)

    def show(self) -> str:
        """
        Returns a string  of the non-stocked product.
        """
        return f"{self._name} (Non-Stocked), Price: {self._price}"

    def buy(self, quantity: int) -> float:
        """
        Cannot buy a non-stocked product.
        """
        raise Exception("Non-stocked products cannot be bought.")


class LimitedProduct(Product):
    """
        Represents a product that is  limited stocked.
     """

    def __init__(self, name: str, price: float, quantity: int, maximum: int):
        super().__init__(name, price, quantity)
        self._maximum = maximum

    def show(self) -> str:
        """
        Returns a string  of the non-stocked product.
        """
        return f"{self._name} (Limited), Price: {self._price}, Quantity: {self._quantity}, Max Purchase: {self._maximum}"

    def buy(self, quantity: int) -> float:
        if quantity > self._maximum:
            raise ValueError(f"Cannot buy more than {self._maximum} of this product.")
        return super().buy(quantity)
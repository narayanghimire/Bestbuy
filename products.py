class Product:
    def __init__(self, name: str, price: float, quantity: int):
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
        return self._quantity

    def set_quantity(self, quantity: int):
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self._quantity = quantity
        if self._quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        return self._active

    def activate(self):
        self._active = True

    def deactivate(self):
        self._active = False

    def show(self) -> str:
        return f"{self._name}, Price: {self._price}, Quantity: {self._quantity}"

    def buy(self, quantity: int) -> float:
        if not self._active:
            raise Exception("Product is not active.")
        if quantity <= 0:
            raise ValueError("Quantity to buy must be positive.")
        if quantity > self._quantity:
            raise ValueError("Not enough stock to complete the purchase.")

        total_price = quantity * self._price
        self.set_quantity(self._quantity - quantity)
        return total_price

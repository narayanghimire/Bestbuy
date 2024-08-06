from abc import ABC, abstractmethod


class Promotion(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity: int) -> float:
        """
        Applies the promotion to a product and returns the discount price.
        """
        pass


class PercentageDiscountPromotion(Promotion):
    def __init__(self, name: str, discount_percentage: float):
        super().__init__(name)
        self.discount_percentage = discount_percentage

    def apply_promotion(self, product, quantity: int) -> float:
        """
        Applies a percentage discount to the product.
        """
        total_price = product.price * quantity
        discount_amount = (self.discount_percentage / 100) * total_price
        return total_price - discount_amount


class BuyTwoGetOneFreePromotion(Promotion):
    def __init__(self, name: str):
        super().__init__(name)

    def apply_promotion(self, product, quantity: int) -> float:
        """
        Applies the buy 2, get 1 free promotion.
        """
        num_full_price_items = quantity - (quantity // 3)
        total_price = num_full_price_items * product.price
        return total_price

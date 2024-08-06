from products import Product
from store import Store


def list_all_products(store):
    """
       List all active products in the store.
    """
    products = store.get_all_products()
    for product in products:
        print(product.show())


def show_total_amount(store):
    """
       show total amount of products in the store.
    """
    total_quantity = store.get_total_quantity()
    print(f"Total quantity in store: {total_quantity}")


def make_an_order(store):
    """
       make an order and return the total price of the order
    """
    products = store.get_all_products()
    print("Available products:")
    for idx, product in enumerate(products):
        print(f"{idx + 1}. {product.show()}")

    order_list = []
    while True:
        product_choice = input("Enter the product number to order (or empty string to finish): ")
        if product_choice == "":
            break

        try:
            product_choice = int(product_choice)
            if product_choice < 1 or product_choice > len(products):
                print("Invalid choice, please try again.")
                continue

            quantity = int(input("Enter the quantity: "))
            if quantity <= 0:
                print("Quantity must be positive, please try again.")
                continue

            order_list.append((products[product_choice - 1], quantity))
        except ValueError:
            print("Invalid input, please enter numbers only.")
            continue

    if order_list:
        total_price = store.order(order_list)
        print(f"Order made! Total payment: ${total_price}")

def start(store):
    """
        Start the user interface for the store.
    """
    while True:
        print("Store Menu")
        print("----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                list_all_products(store)
            elif choice == 2:
                show_total_amount(store)
            elif choice == 3:
                make_an_order(store)
            elif choice == 4:
                print("Thanks for using the store interface!")
                break
            else:
                print("wrong choice, please try again.")
        except ValueError:
            print("wrong input, please enter a number.")


if __name__ == "__main__":
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250)
    ]
    best_buy = Store(product_list)
    start(best_buy)

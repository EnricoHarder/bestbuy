import products
import store


def make_order(best_buy):
    """Prompt the user to select products and quantities, then place the order."""
    all_products = best_buy.get_all_products()
    print()
    for i, product in enumerate(all_products, 1):
        print(f"{i}. {product}")
    print("\nWhen you want to finish order, enter empty text.")

    shopping_list = []
    while True:
        product_input = input("Which product # do you want? ").strip()
        if product_input == "":
            break
        amount_input = input("What amount do you want? ").strip()
        if amount_input == "":
            break
        try:
            product_num = int(product_input)
            amount = int(amount_input)
            if 1 <= product_num <= len(all_products):
                shopping_list.append((all_products[product_num - 1], amount))
                print("Product added to list!")
            else:
                print("Invalid product number.")
        except ValueError:
            print("Please enter valid numbers.")

    if shopping_list:
        try:
            total = best_buy.order(shopping_list)
            print(f"\nOrder made! Total payment: ${total}")
        except (ValueError, Exception) as err:
            print(f"Error while making order: {err}")


def start(best_buy):
    """Display the store menu and handle user input in a loop."""
    while True:
        print("\n   Store Menu")
        print("   ----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("\nPlease choose a number: ").strip()

        if choice == "1":
            print()
            for i, product in enumerate(best_buy.get_all_products(), 1):
                print(f"{i}. {product}")
        elif choice == "2":
            print(f"\nTotal of {best_buy.get_total_quantity()} items in store.")
        elif choice == "3":
            make_order(best_buy)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please enter 1-4.")


if __name__ == '__main__':
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250),
    ]
    best_buy = store.Store(product_list)
    start(best_buy)

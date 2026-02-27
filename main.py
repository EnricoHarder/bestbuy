import products
from store import Store


def test():
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250),
                    ]

    best_buy = Store(product_list)
    all_products = best_buy.get_all_products()
    print(f"Total quantity: {best_buy.get_total_quantity()}")
    print(f"Order cost: {best_buy.order([(all_products[0], 1), (all_products[1], 2)])}")

    pixel8 = products.Product("Google Pixel 8", price=999, quantity=250)
    best_buy.add_product(pixel8)

    print(f"All products: {best_buy.get_all_products()}")

if __name__ == '__main__':
    test()

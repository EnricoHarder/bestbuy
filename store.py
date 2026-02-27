from products import Product


class Store:
    def __init__(self, products):
        self.products = products

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def get_total_quantity(self) -> int:
        return sum(p.get_quantity() for p in self.products)

    def get_all_products(self) -> list:
        return [p for p in self.products if p.is_active()]

    def order(self, shopping_list) -> float:
        total = 0.0
        for product, quantity in shopping_list:
            total += product.buy(quantity)
        return total

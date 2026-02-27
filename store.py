class Store:
    """Represents a store that holds and manages a collection of products."""

    def __init__(self, products):
        """Initialize the store with a list of products."""
        self.products = products

    def add_product(self, product):
        """Add a product to the store."""
        self.products.append(product)

    def remove_product(self, product):
        """Remove a product from the store."""
        self.products.remove(product)

    def get_total_quantity(self) -> int:
        """Return the total number of items across all products."""
        return sum(p.get_quantity() for p in self.products)

    def get_all_products(self) -> list:
        """Return all active products in the store."""
        return [p for p in self.products if p.is_active()]

    @staticmethod
    def order(shopping_list) -> float:
        """Process a list of (product, quantity) tuples and return the total price."""
        total = 0.0
        for product, quantity in shopping_list:
            total += product.buy(quantity)
        return total

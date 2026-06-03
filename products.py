class Product:
    """Represents a product available in the store."""

    def __init__(self, name, price, quantity):
        """Initialize a product. Raises ValueError for invalid input."""
        if not name:
            raise ValueError("Name darf nicht leer sein.")
        if price < 0:
            raise ValueError("Preis darf nicht negativ sein.")
        if quantity < 0:
            raise ValueError("Menge darf nicht negativ sein.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> int:
        """Return the current quantity in stock."""
        return self.quantity

    def set_quantity(self, quantity):
        """Set the quantity and deactivate the product if it reaches 0."""
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        """Return True if the product is active."""
        return self.active

    def activate(self):
        """Activate the product."""
        self.active = True

    def deactivate(self):
        """Deactivate the product."""
        self.active = False

    def show(self):
        """Print a string representation of the product."""
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity) -> float:
        """Buy a given quantity. Returns total price. Raises exception on invalid input."""
        if quantity <= 0:
            raise ValueError("Kaufmenge muss größer als 0 sein.")
        if not self.active:
            raise Exception("Produkt ist nicht aktiv.")
        if quantity > self.quantity:
            raise ValueError("Nicht genug Lagerbestand.")

        self.set_quantity(self.quantity - quantity)
        return self.price * quantity

    # print object representation in lists!
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name='{self.name}', price={self.price}, quantity={self.quantity})"

    def __str__(self):
        status = "Active" if self.active else "Inactive"
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity} ({status})"


class NonStockedProduct(Product):
    """Represents a non-physical product without stock tracking."""

    def __init__(self, name, price):
        """Initialize a non-stocked product with quantity 0."""
        super().__init__(name, price, quantity=0)

    def set_quantity(self, quantity):
        """Quantity for non-stocked products remains 0."""
        pass

    def buy(self, quantity) -> float:
        """Buy a given quantity without changing stock."""
        if quantity <= 0:
            raise ValueError("Kaufmenge muss größer als 0 sein.")
        if not self.active:
            raise Exception("Produkt ist nicht aktiv.")
        
        return self.price * quantity

    def show(self):
        """Print a string representation for non-stocked products."""
        print(f"{self.name}, Price: {self.price} (Non-Stocked Product)")


class LimitedProduct(Product):
    """Represents a product that can only be bought in limited quantities per order."""

    def __init__(self, name, price, quantity, maximum):
        """Initialize a limited product with a maximum allowed quantity."""
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def buy(self, quantity) -> float:
        """Buy a given quantity, but raise exception if it exceeds the maximum."""
        if quantity > self.maximum:
            raise ValueError(f"Maximal {self.maximum} pro Bestellung erlaubt.")
        return super().buy(quantity)

    def show(self):
        """Print a string representation with the limit."""
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity} (Max {self.maximum} per order)")

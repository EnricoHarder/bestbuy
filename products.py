class Product:
    def __init__(self, name, price, quantity):
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
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity) -> float:
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
        return f"Product(name='{self.name}', price={self.price}, quantity={self.quantity})"

    def __str__(self):
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}" + (" (Active)" if self.active else " (Inactive)")
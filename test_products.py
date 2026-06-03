from products import Product
from store import Store


def run_test(description, func):
    """Führt einen Test aus und gibt Ergebnis mit Beschreibung aus."""
    try:
        func()
        print(f"  PASS  {description}")
    except AssertionError as e:
        print(f"  FAIL  {description}: {e}")
    except Exception as e:
        print(f"  ERROR {description}: {e}")


# ---------------------------------------------------------------------------
# Product-Tests
# ---------------------------------------------------------------------------

def test_product_creation_valid():
    """Gültiges Produkt kann erstellt werden."""
    p = Product("MacBook", price=1000, quantity=5)
    assert p.name == "MacBook"
    assert p.price == 1000
    assert p.quantity == 5
    assert p.is_active() is True


def test_product_creation_empty_name():
    """Leerer Name wirft ValueError."""
    try:
        Product("", price=100, quantity=10)
        assert False, "Keine Exception ausgelöst"
    except ValueError:
        pass


def test_product_creation_negative_price():
    """Negativer Preis wirft ValueError."""
    try:
        Product("Test", price=-5, quantity=10)
        assert False, "Keine Exception ausgelöst"
    except ValueError:
        pass


def test_product_creation_negative_quantity():
    """Negative Menge wirft ValueError."""
    try:
        Product("Test", price=100, quantity=-3)
        assert False, "Keine Exception ausgelöst"
    except ValueError:
        pass


def test_buy_normal():
    """Kauf einer gültigen Menge gibt korrekten Preis zurück und aktualisiert Lager."""
    p = Product("Earbuds", price=250, quantity=100)
    total = p.buy(10)
    assert total == 2500
    assert p.get_quantity() == 90


def test_buy_zero_quantity():
    """Kauf mit Menge 0 wirft ValueError."""
    p = Product("Earbuds", price=250, quantity=100)
    try:
        p.buy(0)
        assert False, "Keine Exception ausgelöst"
    except ValueError:
        pass


def test_buy_too_large_quantity():
    """Kauf von mehr als verfügbar wirft ValueError."""
    p = Product("Earbuds", price=250, quantity=10)
    try:
        p.buy(999)
        assert False, "Keine Exception ausgelöst"
    except ValueError:
        pass


def test_product_deactivated_when_sold_out():
    """Produkt wird automatisch deaktiviert wenn Menge 0 erreicht."""
    p = Product("Pixel", price=500, quantity=1)
    p.buy(1)
    assert p.get_quantity() == 0
    assert p.is_active() is False


def test_buy_inactive_product():
    """Kauf eines inaktiven Produkts wirft Exception (nicht 'Lagerbestand')."""
    p = Product("Pixel", price=500, quantity=1)
    p.buy(1)  # Produkt wird deaktiviert
    try:
        p.buy(1)
        assert False, "Keine Exception ausgelöst"
    except Exception as e:
        assert "aktiv" in str(e).lower(), f"Falsche Fehlermeldung: {e}"


def test_activate_deactivate():
    """Produkt kann manuell aktiviert und deaktiviert werden."""
    p = Product("Test", price=10, quantity=5)
    p.deactivate()
    assert p.is_active() is False
    p.activate()
    assert p.is_active() is True


# ---------------------------------------------------------------------------
# Store-Tests
# ---------------------------------------------------------------------------

def test_store_total_quantity():
    """get_total_quantity gibt Summe aller Lagermengen zurück."""
    store = Store([
        Product("A", price=10, quantity=100),
        Product("B", price=20, quantity=200),
    ])
    assert store.get_total_quantity() == 300


def test_store_get_all_products_only_active():
    """get_all_products gibt nur aktive Produkte zurück."""
    p1 = Product("Aktiv", price=10, quantity=5)
    p2 = Product("Inaktiv", price=10, quantity=1)
    p2.deactivate()
    store = Store([p1, p2])
    active = store.get_all_products()
    assert len(active) == 1
    assert active[0].name == "Aktiv"


def test_store_add_remove_product():
    """Produkte können hinzugefügt und entfernt werden."""
    p1 = Product("A", price=10, quantity=5)
    p2 = Product("B", price=20, quantity=3)
    store = Store([p1])
    store.add_product(p2)
    assert len(store.get_all_products()) == 2
    store.remove_product(p1)
    assert len(store.get_all_products()) == 1
    assert store.get_all_products()[0].name == "B"


def test_store_order():
    """order gibt korrekten Gesamtpreis zurück."""
    p1 = Product("Mac", price=1450, quantity=100)
    p2 = Product("Bose", price=250, quantity=500)
    store = Store([p1, p2])
    total = store.order([(p1, 1), (p2, 2)])
    assert total == 1450 + 500, f"Erwartet 1950, bekommen {total}"


# ---------------------------------------------------------------------------
# Alle Tests ausführen
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("=== Product-Tests ===")
    run_test("Gültiges Produkt erstellen",          test_product_creation_valid)
    run_test("Leerer Name -> ValueError",           test_product_creation_empty_name)
    run_test("Negativer Preis -> ValueError",       test_product_creation_negative_price)
    run_test("Negative Menge -> ValueError",        test_product_creation_negative_quantity)
    run_test("Normaler Kauf",                       test_buy_normal)
    run_test("Kauf mit Menge 0 -> ValueError",      test_buy_zero_quantity)
    run_test("Zu große Menge -> ValueError",        test_buy_too_large_quantity)
    run_test("Produkt wird bei 0 deaktiviert",      test_product_deactivated_when_sold_out)
    run_test("Inaktives Produkt kaufen -> Exception", test_buy_inactive_product)
    run_test("Aktivieren / Deaktivieren",           test_activate_deactivate)

    print()
    print("=== Store-Tests ===")
    run_test("Gesamtmenge berechnen",               test_store_total_quantity)
    run_test("Nur aktive Produkte zurückgeben",     test_store_get_all_products_only_active)
    run_test("Produkt hinzufügen und entfernen",    test_store_add_remove_product)
    run_test("Bestellung aufgeben",                 test_store_order)
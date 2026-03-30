from pages.inventory_page import InventoryPage


def test_add_multiple_items(logged_in_page):
    inventory_page= InventoryPage(logged_in_page)
    inventory_page.add_multiple_items(4)

    assert inventory_page.get_cart_count() == '4'

def test_add_specific_item(logged_in_page):

    inventory_page = InventoryPage(logged_in_page)
    inventory_page.add_item_by_name("Sauce Labs Backpack")
    assert inventory_page.get_cart_count() == "1"

def test_add_multiple_specific_item(logged_in_page):
    inventory_page= InventoryPage(logged_in_page)

    inventory_page.add_items_by_names([
        "Sauce Labs Backpack",
        "Sauce Labs Bike Light"
    ])
    assert inventory_page.get_cart_count() == "2"
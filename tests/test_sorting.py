from pages.inventory_page import InventoryPage


def test_sort_price_low_to_high(logged_in_page):

    inventory_page = InventoryPage(logged_in_page)
    inventory_page.sort_items("Price (low to high)")
    prices = inventory_page.get_all_prices()

    assert inventory_page.is_sorted_ascending(prices)

def test_sort_price_high_to_low(logged_in_page):

    inventory_page = InventoryPage(logged_in_page)
    inventory_page.sort_items("Price (high to low)")
    prices = inventory_page.get_all_prices()

    assert inventory_page.is_sorted_descending(prices)

def test_sort_name_a_to_z(logged_in_page):

    inventory_page = InventoryPage(logged_in_page)
    inventory_page.sort_items("Name (A to Z)")
    names = inventory_page.get_all_names()

    assert inventory_page.is_sorted_ascending(names)

def test_sort_name_z_to_a(logged_in_page):

    inventory_page = InventoryPage(logged_in_page)
    inventory_page.sort_items("Name (Z to A)")
    names = inventory_page.get_all_names()

    assert inventory_page.is_sorted_descending(names)



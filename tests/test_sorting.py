from pages.inventory_page import InventoryPage


def test_sort_price_low_to_high(logged_in_page):

    inventory_page = InventoryPage(logged_in_page)
    inventory_page.sort_items("Price (low to high)")
    prices = inventory_page.get_all_prices()

    assert prices == sorted(prices)

def test_sort_price_high_to_low(logged_in_page):

    inventory_page = InventoryPage(logged_in_page)
    inventory_page.sort_items("Price (high to low)")
    prices = inventory_page.get_all_prices()

    assert prices == sorted(prices, reverse=True)



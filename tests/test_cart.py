from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from utils.config import BASE_URL,USERNAME, PASSWORD


def test_cart_validation(logged_in_page):
    # login_page= LoginPage(page)
    # login_page.navigate(BASE_URL)
    # login_page.login(USERNAME, PASSWORD)

    inventory_page = InventoryPage(logged_in_page)
    item_name= inventory_page.get_first_item_name()#to check later if the name and price added are same in cart
    item_price= inventory_page.get_first_item_price()
    inventory_page.add_item_to_cart()

    inventory_page.go_to_cart()

    cart_page= CartPage(logged_in_page)

    assert cart_page.get_cart_items_count() == 1 #if only 1 item is added

    assert cart_page.get_item_name() == item_name
    assert cart_page.get_item_price() == item_price

def test_validate_cart_items_with_price(logged_in_page):

    inventory_page = InventoryPage(logged_in_page)

    items_to_add = [
        "Sauce Labs Backpack",
        "Sauce Labs Bike Light"
    ]

    inventory_page.add_items_by_names(items_to_add)
    inventory_page.go_to_cart()

    cart_page = CartPage(logged_in_page)

    cart_names = cart_page.get_all_item_names()
    cart_prices = cart_page.get_all_item_prices()

    # Basic validations
    assert len(cart_names) == 2
    assert len(cart_prices) == 2

    for item in items_to_add:
        assert item in cart_names
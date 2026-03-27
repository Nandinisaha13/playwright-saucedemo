from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from utils.config import BASE_URL,USERNAME, PASSWORD


def test_cart_validation(page):
    login_page= LoginPage(page)
    login_page.navigate(BASE_URL)
    login_page.login(USERNAME, PASSWORD)

    inventory_page= InventoryPage(page)
    item_name= inventory_page.get_first_item_name()#to check later if the name and price added are same in cart
    item_price= inventory_page.get_first_item_price()
    inventory_page.add_item_to_cart()

    inventory_page.go_to_cart()

    cart_page= CartPage(page)

    assert cart_page.get_cart_items_count() == 1 #if only 1 item is added

    assert cart_page.get_item_name() == item_name
    assert cart_page.get_item_price() == item_price

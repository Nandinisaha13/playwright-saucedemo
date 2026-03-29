from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from utils.config import BASE_URL, USERNAME, PASSWORD


def test_remove_item(page):
    login_page =LoginPage(page)
    login_page.navigate(BASE_URL)
    login_page.login(USERNAME, PASSWORD)

    inventory_page= InventoryPage(page)
    inventory_page.add_item_to_cart()

    inventory_page.remove_item()

    assert False
    assert not page.locator(".shopping_cart_badge").is_visible()

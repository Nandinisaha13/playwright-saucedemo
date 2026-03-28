from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from utils.config import BASE_URL,USERNAME, PASSWORD


def test_checkout(page):

    login_page=LoginPage(page)
    login_page.navigate(BASE_URL)
    login_page.login(USERNAME, PASSWORD)

    inventory_page= InventoryPage(page)
    inventory_page.add_item_to_cart()
    inventory_page.go_to_cart()
    #page.screenshot(path="manual.png")

    cart_page= CartPage(page)
    cart_page.click_checkout()

    checkout_page=CheckoutPage(page)
    checkout_page.fill_info("Demo", "User", "90494")
    checkout_page.continue_checkout()
    checkout_page.finish_checkout()

    assert "thank you" in checkout_page.get_success_message().lower()


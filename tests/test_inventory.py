from pages.login_page import LoginPage
from utils.config import BASE_URL, USERNAME, PASSWORD
from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage

def test_add_to_cart(page) :
    login_page= LoginPage(page)
    login_page.navigate(BASE_URL)
    login_page.login(USERNAME, PASSWORD)#login to valid creds

    invenory_page= InventoryPage(page)
    invenory_page.add_item_to_cart()#adding item to cart

    assert invenory_page.get_cart_count()=='1'#check the count

    invenory_page.go_to_cart()#go to cart for checking the count

    cart_page= CartPage(page)
    assert cart_page.get_cart_items_count() == 1#check the item count on cart page


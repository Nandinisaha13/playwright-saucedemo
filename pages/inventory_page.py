class InventoryPage:

    def __init__(self,page):
        self.page=page
        self.add_to_cart_btn= "#add-to-cart-sauce-labs-backpack"
        self.cart_badge= ".shopping_cart_badge"
        self.cart_icon= ".shopping_cart_link"

    def add_item_to_cart(self):
        self.page.locator(self.add_to_cart_btn).click()

    def get_cart_count(self):
        return self.page.locator(self.cart_badge).inner_text()
    
    def go_to_cart(self):
        self.page.click(self.cart_icon)

    def get_first_item_name(self):
        return self.page.locator(".inventory_item_name").first.inner_text()
    
    def get_first_item_price(self):
        return self.page.locator(".inventory_item_price").first.inner_text()
    
    def remove_item(self):
        self.page.locator("#remove-sauce-labs-backpack").click()
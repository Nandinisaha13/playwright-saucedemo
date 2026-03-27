class CartPage:

    def __init__(self, page):
        self.page= page
        self.cart_items= ".cart_item"

    def  get_cart_items_count(self):
        return len(self.page.locator(self.cart_items).all())
    
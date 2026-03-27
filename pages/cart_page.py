class CartPage:

    def __init__(self, page):
        self.page= page
        self.cart_items= ".cart_item"
        self.first_item_name=".inventory_item_name"
        self.first_item_price=".inventory_item_price"

    def  get_cart_items_count(self):
        return len(self.page.locator(self.cart_items).all())
    
    def get_item_name(self):
        return self.page.locator(self.first_item_name).first.inner_text()
    
    def get_item_price(self):
        return self.page.locator(self.first_item_price).first.inner_text()
  
    
    
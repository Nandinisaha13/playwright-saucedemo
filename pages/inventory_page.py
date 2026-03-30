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

    def add_multiple_items(self, count):
        #items= self.page.locator('[data-test^="add-to-cart"]').all()#using this because evry add have this at starting
        for i in range(count):
            self.page.locator('[data-test^="add-to-cart"]').first.click() #this works better because DOM changes in loop and everything becomes first once added

    def add_item_by_name(self,product_name):
        item=self.page.locator(".inventory_item", has_text= product_name)
        item.locator("button").click()

    def add_items_by_names(self, product_name):
        for name in product_name:
            self.add_item_by_name(name)


            


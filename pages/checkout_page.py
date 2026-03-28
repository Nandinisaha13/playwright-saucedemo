class CheckoutPage:
    def __init__(self, page):
        self.page= page

        self.first_name= "#first-name"
        self.last_name= "#last-name"
        self.postal_code= "#postal-code"
        self.continue_btn= "#continue"

        self.finish_button= "#finish"
        self.success_message= ".complete-header"

    def fill_info(self, first, last, zip_code):
        self.page.fill(self.first_name, first)
        self.page.fill(self.last_name, last)
        self.page.fill(self.postal_code, zip_code)
        
    def continue_checkout(self):
        self.page.click(self.continue_btn)
    
    def finish_checkout(self):
        self.page.click(self.finish_button)

    def get_success_message(self):
        return self.page.locator(self.success_message).inner_text()
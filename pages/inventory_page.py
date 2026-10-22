class InventoryPage:

    def __init__(self, page):

        self.page = page

        self.inventory_title = page.locator(".title")

    def get_title(self):

        return self.inventory_title.text_content()



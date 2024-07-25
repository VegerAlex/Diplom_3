from locators.order_feed_page_locators import OrderFeedPageLocators

class OrderFeedPage:
    def __init__(self, driver):
        self.driver = driver

    def open_order_details(self):
        order_item = self.driver.find_element(*OrderFeedPageLocators.ORDER_ITEM)
        order_item.click()

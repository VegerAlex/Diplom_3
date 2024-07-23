from locators.constructor_page_locators import ConstructorPageLocators

class ConstructorPage:
    def __init__(self, driver):
        self.driver = driver

    def add_ingredient_to_order(self):
        ingredient_item = self.driver.find_element(*ConstructorPageLocators.INGREDIENT_ITEM)
        ingredient_item.click()

    def place_order(self):
        place_order_button = self.driver.find_element(*ConstructorPageLocators.PLACE_ORDER_BUTTON)
        place_order_button.click()

    def close_modal(self):
        close_modal_button = self.driver.find_element(*ConstructorPageLocators.CLOSE_MODAL_BUTTON)
        close_modal_button.click()

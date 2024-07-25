from locators.personal_account_page_locators import PersonalAccountPageLocators

class PersonalAccountPage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_order_history(self):
        order_history_button = self.driver.find_element(*PersonalAccountPageLocators.ORDER_HISTORY_BUTTON)
        order_history_button.click()

    def logout(self):
        logout_button = self.driver.find_element(*PersonalAccountPageLocators.LOGOUT_BUTTON)
        logout_button.click()

from locators.main_page_locators import MainPageLocators

class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_login_page(self):
        login_button = self.driver.find_element(*MainPageLocators.LOGIN_BUTTON)
        login_button.click()

    def go_to_personal_account(self):
        personal_account_button = self.driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        personal_account_button.click()

    def go_to_constructor(self):
        constructor_button = self.driver.find_element(*MainPageLocators.CONSTRUCTOR_BUTTON)
        constructor_button.click()

    def go_to_order_feed(self):
        order_feed_button = self.driver.find_element(*MainPageLocators.ORDER_FEED_BUTTON)
        order_feed_button.click()

    def go_to_restore_password(self):
        restore_password_button = self.driver.find_element(*MainPageLocators.RESTORE_PASSWORD_BUTTON)
        restore_password_button.click()
